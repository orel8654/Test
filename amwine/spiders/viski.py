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

    def parse(self, response, **kwargs):

        category_items = ['Главная страница', 'Каталог', 'Крепкие напитки', 'Виски']

        for item in range(len(response.json()['products'])):

            products = response.json()['products'][item]

            try:
                title = products['name']
                value = str(products['props']['value'])
                name = {
                    'name': title,
                    'value': value,
                }
            except Exception:
                title = products['name']
                name = {
                    'name': title,
                }

            try:
                brand = str(products['props']['brand'])
            except Exception:
                brand = str(None)

            sale = products['sale']
            if sale == False:
                try:
                    price_data = {
                        'current': float(products['price']),
                        'original': float(products['price']),
                        'sale': 'Скидка 0%',
                    }
                except Exception:
                    try:
                        price_data = {
                            'current': float(products['props']['middle_price_77']),
                            'original': float(products['props']['middle_price_77']),
                            'sale': 'Скидка 0%',
                        }
                    except Exception:
                        try:
                            price_data = {
                                'current': float(products['old_price_77']),
                                'original': float(products['old_price_77']),
                                'sale': 'Скидка 0%',
                            }
                        except Exception:
                            price_data = {
                                'current': None,
                                'original': None,
                                'sale': 'Скидка 0%',
                            }
            else:
                try:
                    price_data = {
                        'current': products['price'],
                        'original': products['old_price'],
                        'sale': f'Скидка {sale}',
                    }
                except Exception:
                    price_data = {
                        'current': products['props']['middle_price_77'],
                        'original': products['props']['old_price_77'],
                        'sale': f'Скидка {sale}',
                    }

            try:
                artic = str(products['props']['article'])
            except Exception:
                artic = str(None)

            try:
                country = products['props']['country']
            except Exception:
                country = str(None)

            yield {
                'time': datetime.now().timestamp(),
                'RPC': str(products['id']),
                'url': 'https://amwine.ru' + products['link'],
                'title': name,
                'brand': brand,
                'section': category_items,
                'price_data': price_data,
                'stock': {
                    'in_stock': products['available'],
                },
                'assets': {
                    'main_image': 'https://amwine.ru' + products['preview_picture'],
                },
                'metadata': {
                    'АРТИКУЛ': artic,
                    'ОБЪЕМ': value,
                    'СТРАНА ПРОИЗВОДИТЕЛЬ': country,
                },
                'variants': 1,
            }
