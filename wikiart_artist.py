import scrapy

from bs4 import BeautifulSoup

from items import ArtistItem


class WikiArtArtistSpider(scrapy.Spider):
    name = "wikiart_artist"
    allowed_domains = ["wikiart.org"]
    start_urls = ["https://www.wikiart.org/en/artists-by-nation"]
    id = 0

    def parse(self, response):
        for nation in response.xpath('//main/ul/li/a/@href').getall():
            yield response.follow(nation + "/text-list", callback=self.parse_nation)

    def parse_nation(self, response):
        for artist in response.xpath('//main/div/ul/li/a/@href').getall():
            yield response.follow(artist, callback=self.parse_artist)

    def parse_artist(self, response):
        name_raw = response.xpath('//main/div/article/h3/text()')
        name = name_raw.get().replace("  ", '').replace('\n', '') if name_raw else name_raw
        original_name_raw = response.xpath('//main/div/article/h4/text()').get()
        original_name = original_name_raw.replace("  ", '').replace('\n', '') if original_name_raw else original_name_raw

        birth_date = response.xpath('//main/div/article/ul/li/span[@itemprop="birthDate"]/text()').get()
        birth_place = response.xpath('//main/div/article/ul/li/span[@itemprop="birthPlace"]/text()').get()

        death_date = response.xpath('//main/div/article/ul/li/span[@itemprop="deathDate"]/text()').get()
        death_place = response.xpath('//main/div/article/ul/li/span[@itemprop="deathPlace"]/text()').get()

        active_years_raw = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Active Years:")]]]').get()
        active_years = active_years_raw.replace("<li>\n            <s>Active Years:</s>\n            ", '')\
            .replace("\n        </li>", '') if active_years_raw else active_years_raw

        nationality = response.xpath('//span[@itemprop="nationality"]/text()').get()

        art_movements = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Art Movement:")]]]/span/a/text()').getall()
        painting_school = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Painting School:")]]]/span/a/text()').getall()

        genres = response.xpath('//span[@itemprop="genre"]/text()').getall()
        fields = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Field:")]]]/span/a/text()').getall()

        influenced_by = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Influenced by:")]]]/a/text()').getall()
        influenced_on = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Influenced on:")]]]/a/text()').getall()

        teachers = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Teachers:")]]]/a/text()').getall()
        pupils = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Pupils:")]]]/a/text()').getall()

        art_institutions = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Art institution:")]]]/a/text()').getall()

        friends_and_coworkers = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Friends and Co-workers:")]]]/a/text()').getall()

        wikipedia_link = response.xpath('//main/div/article/ul/li[.//s[text()[contains(.,"Wikipedia:")]]]/a/@href').get()

        description_raw = response.xpath('//p[@itemprop="description"]').get()
        description = BeautifulSoup(description_raw, features="lxml").get_text() if description_raw else description_raw

        wiki_description_raw = response.xpath('//div[@id="info-tab-wikipediaArticle"]/p').get()
        wiki_description = BeautifulSoup(wiki_description_raw, features="lxml").get_text() if wiki_description_raw else wiki_description_raw

        yield ArtistItem({
            "Id": self.id,
            "URL": response.url,
            "Name": name,
            "OriginalName": original_name,
            "BirthDate": birth_date,
            "BirthPlace": birth_place,
            "DeathDate": death_date,
            "DeathPlace": death_place,
            "ActiveYears": active_years,
            "Nationality": nationality,
            "ArtMovements": art_movements,
            "PaintingSchool": painting_school,
            "Genres": genres,
            "Fields": fields,
            "InfluencedOn": influenced_on,
            "InfluencedBy": influenced_by,
            "Teachers": teachers,
            "Pupils": pupils,
            "ArtInstitutions": art_institutions,
            "FriendsAndCoworkers": friends_and_coworkers,
            "WikipediaLink": wikipedia_link,
            "Description": description,
            "WikiDescription": wiki_description,
        })

        self.id += 1

