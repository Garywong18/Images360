# -*- coding: utf-8 -*-
import scrapy
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/zjl?ch=beauty&sn=30&listtype=new&temp=1']

    def start_requests(self):
        base_url = 'http://images.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
        for page in range(1,self.settings['MAX_PAGE']+1):
            url = base_url.format(page*30)
            yield scrapy.Request(
                url,
                callback=self.parse
            )
    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = {}
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('title')
            yield item