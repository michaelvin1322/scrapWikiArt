from duck_duck_go import DuckDuckGoSpider
from ScrapWikiArt.items import UpdatedMovementItem


class DuckDuckGoMovementSpider(DuckDuckGoSpider):
    name = 'duck_duck_go_movement'
    allowed_domains = ['api.duckduckgo.com']

    item_class = UpdatedMovementItem
    query_feature = 'Name'
