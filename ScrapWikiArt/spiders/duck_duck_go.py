import scrapy
import json
import pandas as pd
from ScrapWikiArt.items import ImageItem


class MySpider(scrapy.Spider):
    name = 'duck_duck_go'
    allowed_domains = ['api.duckduckgo.com']

    def __init__(self, input_file=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.input_file = input_file

    def start_requests(self):
        if self.input_file is None:
            raise scrapy.exceptions.CloseSpider('Input file not specified')

        # Read the input file using Pandas
        df = pd.read_csv(self.input_file, low_memory=False)

        # Filter out rows that already have a description or WikiDescription
        df_filtered = df[df["Description"].isna() & df["WikiDescription"].isna()]

        for row_dict in df_filtered.to_dict(orient="records"):
            query = row_dict['Title']
            url = f'http://api.duckduckgo.com/?q={query}&format=json'
            yield scrapy.Request(url, meta={'row': row_dict}, callback=self.parse)

    def parse(self, response):
        row_dict = response.meta['row']
        try:
            data = json.loads(response.text)
            if not ('Abstract' in data and 'AbstractURL' in data):
                self.retry_request(response)

            if data['Abstract'] != '':
                row_dict["WikiLink"] = data["AbstractURL"]
                row_dict["WikiDescription"] = data["Abstract"]
                row_dict["image_urls"] = []
                row_dict.pop("images", None)
                yield ImageItem(row_dict)

            self.retry_request(response)
        except json.JSONDecodeError:
            self.retry_request(response)

    def retry_request(self, response):
        retry_count = response.meta.get('retry_count', 0)
        if retry_count < 5:  # Set your max retry limit
            retry_count += 1
            yield scrapy.Request(response.url, meta={'row': response.meta['row'], 'retry_count': retry_count}, callback=self.parse, dont_filter=True)

