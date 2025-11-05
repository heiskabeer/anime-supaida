import scrapy


class ActionspiderSpider(scrapy.Spider):
    name = "actionspider"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/anime/genre/1/Action"]

    def parse(self, response):
        pass
