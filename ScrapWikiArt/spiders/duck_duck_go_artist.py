from duck_duck_go import DuckDuckGoSpider
from ScrapWikiArt.items import ArtistItem


class DuckDuckGoArtistSpider(DuckDuckGoSpider):
    name = 'duck_duck_go_artist'
    allowed_domains = ['api.duckduckgo.com']

    item_class = ArtistItem
    query_feature = 'Name'
