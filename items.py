import scrapy


class WikiArtItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
