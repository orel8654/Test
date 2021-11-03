import scrapy
from scrapy.http.request import Request
from scrapy.http import FormRequest, headers
from curl import *

class ViskiSpider(scrapy.Spider):
    name = 'viski'
    allowed_domains = ['amwine.ru']
    # start_urls = ['https://amwine.ru/catalog/krepkie_napitki/viski/?page=1']
    start_urls = ['https://amwine.ru/local/components/adinadin/catalog.section.json/ajax_call.php']
    pages_count = 0

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            method='POST',
            dont_filter=True,
            cookies=cookies,
            headers=headers,
            body=body,
        )





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