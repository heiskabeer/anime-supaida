import scrapy


class ActionspiderSpider(scrapy.Spider):
    name = "actionspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/anime/genre/1/Action"]

    def parse(self, response):
        animes = response.css('div.js-anime-category-producer')
        for anime in animes:
            yield {
                'title': anime.css('h2.h2_anime_title a::text').get(),
                'year_aired': anime.css('div.prodsrc span.item::text').get().split(',')[1].strip(),
                'status': anime.css('div.prodsrc span.finished::text').get() or anime.css('div.prodsrc span.airing::text').get(),
                'episodes': anime.css('div.prodsrc span.item:nth-of-type(3) > span::text').get().split()[0],
                'image_url': anime.css('div.image img').attrib['data-src'],
                'profile_url': anime.css('div.image a::attr(href)').get(),
                'studio': anime.css('div.properties > div.property:nth-of-type(1) a::text').get(),
                'source': anime.css('div.properties > div.property:nth-of-type(2) span.item::text').get(),
                'theme': anime.css('div.properties > div.property:nth-of-type(3) span.item a::text').getall() or '',
                'demographic': anime.css('div.properties > div.property:nth-of-type(4) span.item a::text').get(),
                'ratings': anime.css('div.scormem-item.score.score-label *::text').getall()[1].strip(),
                'fanbase':  anime.css('div.scormem-item.member *::text').getall()[1].strip()
            }
