import scrapy
from scrapy import log
from tutorial.items import TutorialItem
class DemzSpider(scrapy.Spider):
    name='test'
    start_urls = [
        "http://news.163.com/16/1107/15/C59GQULA00014AEE.html"
    ]

    def parse(self,response):
        item=TutorialItem()
        item['image_urls']=filter(lambda x:x.startswith('http'),response.xpath('//img/@src').extract())
        yield item


