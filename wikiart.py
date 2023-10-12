import scrapy
import hashlib

from bs4 import BeautifulSoup

from items import ImageItem
# from settings import IMAGES_STORE


class WikiArtSpider(scrapy.Spider):
    name = "wikiart"
    allowed_domains = ["wikiart.org"]
    domain = "wikiart.org"
    start_urls = ["https://www.wikiart.org/en/artists-by-nation"]
    id = 0
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy.pipelines.images.ImagesPipeline': 1,
        },
        # "IMAGES_STORE": IMAGES_STORE,
        "IMAGES_STORE": "data/img",
    }

    def parse(self, response):
        for nation in response.xpath('//main/ul/li/a/@href').getall():
            yield response.follow(nation + "/text-list", callback=self.parse_nation)

    def parse_nation(self, response):
        for artist in response.xpath('//main/div/ul/li/a/@href').getall():
            yield response.follow(artist + "/all-works/text-list", callback=self.parse_artist)

    def parse_artist(self, response):
        for item in response.xpath('//main/div/ul/li/a/@href').getall():
            yield response.follow(item, callback=self.parse_item)

    def parse_item(self, response):
        url = response.url
        title = response.xpath("//article/h3/text()").get()
        original_title_raw = response.xpath("//li[.//s[text()[contains(.,'Original Title:')]]]").get()
        original_title = original_title_raw.replace("<li>\n            <s>Original Title:</s>\n            ", '')\
            .replace("\n        </li>", '') if original_title_raw else original_title_raw

        author = response.xpath("//article/h5[@itemprop='creator']/span[@itemprop='name']/a/text()").get()
        author_link = self.domain + response.xpath("//article/h5[@itemprop='creator']/span[@itemprop='name']/a/@href").get()
        date = response.xpath("//li[.//s[text()[contains(.,'Date:')]]]/span[@itemprop='dateCreated']/text()").get()

        styles_names = response.xpath("//li[.//s[text()[contains(.,'Style:')]]]/span/a/text()").getall()
        styles_links = map(
            lambda style_url: self.domain + style_url,
            response.xpath("//li[.//s[text()[contains(.,'Style:')]]]/span/a/@href").getall()
        )
        styles = list(zip(styles_names, styles_links))

        series = response.xpath("//li[.//s[text()[contains(.,'Series:')]]]/a/text()").get()
        series_link = response.xpath("//li[.//s[text()[contains(.,'Series:')]]]/a/@href").get()

        genre = response.xpath("//li[.//s[text()[contains(.,'Genre:')]]]/span/a/span[@itemprop='genre']/text()").get()
        genre_link = self.domain + response.xpath("//li[.//s[text()[contains(.,'Genre:')]]]/span/a/@href").get()

        media = response.xpath("//li[.//s[text()[contains(.,'Media:')]]]/span/a/text()").getall()
        location = response.xpath("//li[.//s[text()[contains(.,'Location:')]]]/span/text()").get()

        dimensions_raw = response.xpath("//li[.//s[text()[contains(.,'Dimensions')]]]").get()
        dimensions = dimensions_raw.replace('<li>\n            <s class="title">Dimensions:</s>\n            ', '')\
            .replace("\n        </li>", '') if dimensions_raw else dimensions_raw

        description_raw = response.xpath('//div[@id="info-tab-description"]/p').get()
        description = BeautifulSoup(description_raw, features="lxml").get_text() if description_raw else description_raw

        wiki_description_raw = response.xpath('//div[@id="info-tab-wikipediadescription"]/p').get()
        wiki_description = BeautifulSoup(wiki_description_raw, features="lxml").get_text() if wiki_description_raw else wiki_description_raw

        wiki_link = response.xpath('//a[@class="wiki-link"]/@href').get()

        tags = response.xpath("//div[@class='tags-cheaps']/div/a/text()").getall()
        tags = [tag.replace('\n', '').replace('\t', '').replace(' ', '') for tag in tags]

        img_urls = response.xpath('//ul[@class="image-variants-container"]//a/@data-image-url').getall()

        if not img_urls:
            img_urls = [response.xpath('//img[@itemprop="image"]/@src').get()]
        # img = f"img/full/{hashlib.sha1(img_url.encode()).hexdigest()}.{img_url.split('.')[-1]}"

        yield ImageItem({
            "Id": self.id,
            "URL": url,
            "Title": title,
            "OriginalTitle": original_title,
            "Author": author,
            "AuthorLink": author_link,
            "Date": date,
            "Styles": styles,
            "Series": series,
            "SeriesLink": series_link,
            "Genre": genre,
            "GenreLink": genre_link,
            "Media": media,
            "Location": location,
            "Dimensions": dimensions,
            "Description": description,
            "WikiDescription": wiki_description,
            "WikiLink": wiki_link,
            "Tags": tags,
            "image_urls": img_urls,
        })

        self.id += 1
