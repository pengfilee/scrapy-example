import scrapy
from tutorial.items import TutorialItem
class DemzSpider(scrapy.Spider):
    name='test'
    start_urls = [
        "https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html"
    ]

    def parse(self,response):
        for sel in response.xpath('//ul/li'):
            item=TutorialItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item


