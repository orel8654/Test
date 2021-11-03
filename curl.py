url = 'https://amwine.ru/local/components/adinadin/catalog.section.json/ajax_call.php'

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "ru",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "amwine.ru",
    "Origin": "https://amwine.ru",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Connection": "keep-alive",
    "Referer": "https://amwine.ru/catalog/krepkie_napitki/viski/",
    # "Content-Length": "1148",
    "X-Requested-With": "XMLHttpRequest"
}

cookies = {
    "_fbp": "fb.1.1635854330192.1699125164",
    "_ga": "GA1.2.1973656503.1635854329",
    "_gat_UA-92274077-1": "1",
    "_gid": "GA1.2.1906133224.1635854329",
    "_hjAbsoluteSessionInProgress": "1",
    "_userGUID": "0:kvi1finn:FEigeIWNVY8qaoffb4T1Lj6UjQ7doGTi",
    "AMWINE__GUEST_ID": "91205008",
    "AMWINE__LAST_VISIT": "03.11.2021%2018%3A54%3A27",
    "popmechanic_sbjs_migrations": "popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1",
    "directCrm-session": "%7B%22deviceGuid%22%3A%223dad716e-44f9-4850-85dc-4c69c1301f61%22%7D",
    "mindboxDeviceUUID": "3dad716e-44f9-4850-85dc-4c69c1301f61",
    "_ym_isad": "2",
    "AMWINE__AB_HASH": "3_1",
    "TEST_AMWINE__AB_HASH": "undefined",
    "AMWINE__IS_ADULT": "Y",
    "_hjid": "1e77ce00-de83-41ab-b096-ea390c6b1c9d",
    "_ym_d": "1635854330",
    "_ym_uid": "1635854330568852096",
    "BX_USER_ID": "0a16d9f004a897277adf34d9075b4890",
    "dSesn": "9b753f46-0d6b-bea7-013f-f85cf7a3d3ee",
    "AMWINE__AUTO_GEOSERVICE": "1",
    "AMWINE__CITY_NAME": "%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
    "AMWINE__CITY_SALE_LOCATION_ID": "19",
    "AMWINE__REGION_CODE": "moscow",
    "AMWINE__REGION_ELEMENT_ID": "342",
    "AMWINE__REGION_ELEMENT_XML_ID": "77",
    "PHPSESSID": "s1A8iSw2SUi0VtQCyo5iNez0I3WVsSVA"
}

body = 'json=y&params%5BIBLOCK_TYPE%5D=catalog&params%5BIBLOCK_ID%5D=2&params%5BCACHE_TYPE%5D=Y&params%5BCACHE_TIME%5D=3600&params%5BSECTION_ID%5D=28&params%5BSECTION_CODE%5D=viski&params%5BPRICE_CODE%5D=MOSCOW&params%5BPAGE_ELEMENT_COUNT%5D=18&params%5BFILTER_NAME%5D=arrFilterCatalog&params%5BSORT_ORDER%5D=ASC&params%5BSORT_FIELD%5D=SORT&params%5BMESSAGE_404%5D=&params%5BSET_STATUS_404%5D=&params%5BSHOW_404%5D=Y&params%5BFILE_404%5D=&params%5BNO_INDEX_NO_FOLLOW%5D=N&params%5BCURRENT_PAGE%5D=1&params%5B~IBLOCK_TYPE%5D=catalog&params%5B~IBLOCK_ID%5D=2&params%5B~CACHE_TYPE%5D=Y&params%5B~CACHE_TIME%5D=3600&params%5B~SECTION_ID%5D=28&params%5B~SECTION_CODE%5D=viski&params%5B~PRICE_CODE%5D=MOSCOW&params%5B~PAGE_ELEMENT_COUNT%5D=18&params%5B~FILTER_NAME%5D=arrFilterCatalog&params%5B~SORT_ORDER%5D=ASC&params%5B~SORT_FIELD%5D=SORT&params%5B~MESSAGE_404%5D=&params%5B~SET_STATUS_404%5D=&params%5B~SHOW_404%5D=Y&params%5B~FILE_404%5D=&params%5B~NO_INDEX_NO_FOLLOW%5D=N&params%5B~CURRENT_PAGE%5D=1&current_filter%5BACTIVE%5D=Y&current_filter%5BIBLOCK_ID%5D=2&current_filter%5BINCLUDE_SUBSECTIONS%5D=Y&current_filter%5BSECTION_ID%5D=28&PAGEN_1=1&sort=sort'

# request = Request(
#     url=url,
#     method='POST',
#     dont_filter=True,
#     cookies=cookies,
#     headers=headers,
#     body=body,
# )

# fetch(request)