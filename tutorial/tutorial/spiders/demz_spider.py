import scrapy
from tutorial.items import TutorialItem
class DemzSpider(scrapy.Spider):
    name='test'
    start_urls = [
        "http://news.163.com/16/1107/15/C59GQULA00014AEE.html"
    ]

    def parse(self,response):
        for sel in response.xpath('//p/span'):
            item=TutorialItem()
            item['image_urls'] =['http://cms-bucket.nosdn.127.net/catchpic/5/54/54841f0d54ec20d30f315aaaa8a8585e.png'] 
            yield item


