from duck_duck_go import DuckDuckGoSpider
from ScrapWikiArt.items import UpdatedStyleItem


class DuckDuckGoStyleSpider(DuckDuckGoSpider):
    name = 'duck_duck_go_style'
    allowed_domains = ['api.duckduckgo.com']

    item_class = UpdatedStyleItem
    query_feature = 'Name'
