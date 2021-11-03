import json

import scrapy
from ..items import AmwineItem
from scrapy.loader import ItemLoader


class ViskiSpider(scrapy.Spider):
    name = 'viski'
    allowed_domains = ['amwine.ru']
    start_urls = ['https://amwine.ru/catalog/krepkie_napitki/viski/?page=1']
    pages_count = 0

    cookie = ''
    # name = 'test'
    # allowed_domains = ['magnatiles.com']
    # start_urls = ['https://magnatiles.com/products/page/1/']
    # pages_count = 0


    def parse(self, response):
        pp = response.css('title::text').get().strip()
        yield {
            'pp': pp,
        }





    # def parse(self, response):
    #     for p in response.css('ul.products li'):
    #         # il = ItemLoader(item=AmwineItem(), selector=p)
    #
    #         # il.add_css('scu', 'a.button::attr(data-product_sku)')
    #         # il.add_css('name', 'h2')
    #         # il.add_css('price', 'span.price bdi')
    #
    #         yield  il.load_item()
    #
    #         yield {
    #             'name': p.css('h2::text').get(),
    #             'scu': p.css('a.button::attr(data-product_scu)').get(),
    #             'price': p.css('span.price bdi::text').get(),
    #         }
    #     next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)