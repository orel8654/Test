import scrapy
from scrapy.http.request import Request
from scrapy.http import FormRequest, headers
from curl import *
import math
from datetime import datetime
import json

class ViskiSpider(scrapy.Spider):
    name = 'viski'
    allowed_domains = ['amwine.ru']
    start_urls = ['https://amwine.ru/local/components/adinadin/catalog.section.json/ajax_call.php']
    pages_count = 0

    def max_pages(self, response):
        max_items = response.json()['productsTotalCount']
        items_in_pages = 18
        all_pages = float(max_items) / items_in_pages
        self.pages_count = math.ceil(all_pages)

        for count in range(1, 1 + self.pages_count):
            body = f'json=y&params%5BIBLOCK_TYPE%5D=catalog&params%5BIBLOCK_ID%5D=2&params%5BCACHE_TYPE%5D=Y&params%5BCACHE_TIME%5D=3600&params%5BSECTION_ID%5D=28&params%5BSECTION_CODE%5D=viski&params%5BPRICE_CODE%5D=MOSCOW&params%5BPAGE_ELEMENT_COUNT%5D=18&params%5BFILTER_NAME%5D=arrFilterCatalog&params%5BSORT_ORDER%5D=ASC&params%5BSORT_FIELD%5D=SORT&params%5BMESSAGE_404%5D=&params%5BSET_STATUS_404%5D=&params%5BSHOW_404%5D=Y&params%5BFILE_404%5D=&params%5BNO_INDEX_NO_FOLLOW%5D=N&params%5BCURRENT_PAGE%5D=1&params%5B~IBLOCK_TYPE%5D=catalog&params%5B~IBLOCK_ID%5D=2&params%5B~CACHE_TYPE%5D=Y&params%5B~CACHE_TIME%5D=3600&params%5B~SECTION_ID%5D=28&params%5B~SECTION_CODE%5D=viski&params%5B~PRICE_CODE%5D=MOSCOW&params%5B~PAGE_ELEMENT_COUNT%5D=18&params%5B~FILTER_NAME%5D=arrFilterCatalog&params%5B~SORT_ORDER%5D=ASC&params%5B~SORT_FIELD%5D=SORT&params%5B~MESSAGE_404%5D=&params%5B~SET_STATUS_404%5D=&params%5B~SHOW_404%5D=Y&params%5B~FILE_404%5D=&params%5B~NO_INDEX_NO_FOLLOW%5D=N&params%5B~CURRENT_PAGE%5D=1&current_filter%5BACTIVE%5D=Y&current_filter%5BIBLOCK_ID%5D=2&current_filter%5BINCLUDE_SUBSECTIONS%5D=Y&current_filter%5BSECTION_ID%5D=28&PAGEN_1={count}&sort=sort'
            yield Request(
                url=self.start_urls[0],
                method='POST',
                dont_filter=True,
                cookies=cookies,
                headers=headers,
                body=body,
                callback=self.parse,
            )

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            method='POST',
            dont_filter=True,
            cookies=cookies,
            headers=headers,
            body=body,
            callback=self.max_pages,
        )
        # self.max_pages(request)

    def parse(self, response, **kwargs):

        # time = datetime.now().strftime('%Y-%m-%d %H:%m')
        # time = datetime.now().timestamp()

        category_items = ['Главная страница', 'Каталог', 'Крепкие напитки', 'Виски']

        for item in range(len(response.json()['products'])):
            try:
                title = response.json()['products'][item]['name']
                value = response.json()['products'][item]['props']['value']
                name = {
                    'name': title,
                    'value': value,
                }
            except Exception:
                title = response.json()['products'][item]['name']
                name = {
                    'name': title,
                }

            sale = response.json()['products'][item]['sale']
            if sale != False:
                price_data = {
                    'current': float(response.json()['products'][item]['props']['middle_price_77']),
                    'original': float(response.json()['products'][item]['props']['old_price_77']),
                    'sale': f'Скидка {sale}',
                }
            else:
                price_data = {
                    'current': float(response.json()['products'][item]['props']['old_price_77']),
                    'original': float(response.json()['products'][item]['props']['old_price_77']),
                    'sale': 'Скидка 0%',
                }

            yield {
                'time': datetime.now().timestamp(),
                'RPC': str(response.json()['products'][item]['id']),
                'url': 'https://amwine.ru' + response.json()['products'][item]['link'],
                'title': name,
                'brand': str(response.json()['products'][item]['props']['brand']),
                'section': category_items,
                'price_data': price_data,
                'stock': {
                    'in_stock': response.json()['products'][item]['available'],
                },
                'assets': {
                    'main_image': 'https://amwine.ru' + response.json()['products'][item]['preview_picture'],
                },
                'metadata': {
                    'АРТИКУЛ': response.json()['products'][item]['props']['article'],
                    'СТРАНА ПРОИЗВОДИТЕЛЬ': response.json()['products'][item]['props']['country']
                },
                'variants': 1,
            }

        # yield {
        #     'RPC': response.json()['products'][0]['props']['article']
        # }




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