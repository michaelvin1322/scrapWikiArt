import scrapy


class ImageItem(scrapy.Item):
    Id = scrapy.Field()
    URL = scrapy.Field()
    Title = scrapy.Field()
    OriginalTitle = scrapy.Field()
    Author = scrapy.Field()
    Date = scrapy.Field()
    Styles = scrapy.Field()
    Series = scrapy.Field()
    Genre = scrapy.Field()
    Media = scrapy.Field()
    Location = scrapy.Field()
    Dimensions = scrapy.Field()
    Description = scrapy.Field()
    WikiDescription = scrapy.Field()
    Tags = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

