import scrapy


class ImageItem(scrapy.Item):
    Id = scrapy.Field()
    URL = scrapy.Field()
    Title = scrapy.Field()
    OriginalTitle = scrapy.Field()
    Author = scrapy.Field()
    AuthorLink = scrapy.Field()
    Date = scrapy.Field()
    Styles = scrapy.Field()
    Series = scrapy.Field()
    SeriesLink = scrapy.Field()
    Genre = scrapy.Field()
    GenreLink = scrapy.Field()
    Media = scrapy.Field()
    Location = scrapy.Field()
    Dimensions = scrapy.Field()
    Description = scrapy.Field()
    WikiDescription = scrapy.Field()
    WikiLink = scrapy.Field()
    Tags = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class ArtistItem(scrapy.Item):
    Id = scrapy.Field()
    URL = scrapy.Field()
    Name = scrapy.Field()
    OriginalName = scrapy.Field()
    BirthDate = scrapy.Field()
    BirthPlace = scrapy.Field()
    DeathDate = scrapy.Field()
    DeathPlace = scrapy.Field()
    ActiveYears = scrapy.Field()
    Nationality = scrapy.Field()
    ArtMovements = scrapy.Field()
    PaintingSchool = scrapy.Field()
    Genres = scrapy.Field()
    Fields = scrapy.Field()
    InfluencedOn = scrapy.Field()
    InfluencedBy = scrapy.Field()
    Teachers = scrapy.Field()
    Pupils = scrapy.Field()
    ArtInstitutions = scrapy.Field()
    FriendsAndCoworkers = scrapy.Field()
    Description = scrapy.Field()
    WikiDescription = scrapy.Field()
    WikipediaLink = scrapy.Field()


class StyleItem(scrapy.Item):
    Id = scrapy.Field()
    Name = scrapy.Field()
    Link = scrapy.Field()
    Description = scrapy.Field()


class MovementItem(scrapy.Item):
    Id = scrapy.Field()
    Name = scrapy.Field()
    Link = scrapy.Field()
    Description = scrapy.Field()


class SchoolItem(scrapy.Item):
    Id = scrapy.Field()
    Name = scrapy.Field()
    Link = scrapy.Field()
    Description = scrapy.Field()


