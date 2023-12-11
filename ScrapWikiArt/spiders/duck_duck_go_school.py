from duck_duck_go import DuckDuckGoSpider
from ScrapWikiArt.items import UpdatedSchoolItem


class DuckDuckGoSchoolSpider(DuckDuckGoSpider):
    name = 'duck_duck_go_school'
    allowed_domains = ['api.duckduckgo.com']

    item_class = UpdatedSchoolItem
    query_feature = 'Name'
