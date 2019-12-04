import scrapy
from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    start_urls=[
            'http://quotes.toscrape.com'
            ]

    def parse(self, response):

        items = TutorialItem()
        div_class= response.css("div.quote")


        for quotes in div_class:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            text=quotes.css("span.text::text").extract()
            author=quotes.css(".author::text").extract()
            tag=quotes.css(".tag::text").extract()
            items['title']= text
            items['Author']=author
            items['tags']=tag

            yield items
