# Scrapy settings for amwine project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amwine'

SPIDER_MODULES = ['amwine.spiders']
NEWSPIDER_MODULE = 'amwine.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'amwine (+http://www.amwine.ru)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Cookie': 'IS_ADULT=Y; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.1973656503.1635854329; _gid=GA1.2.1906133224.1635854329; _fbp=fb.1.1635854330192.1699125164; _ym_visorc=w; directCrm-session=%7B%22deviceGuid%22%3A%223dad716e-44f9-4850-85dc-4c69c1301f61%22%7D; mindboxDeviceUUID=3dad716e-44f9-4850-85dc-4c69c1301f61; AMWINE__GUEST_ID=91205008; AMWINE__LAST_VISIT=03.11.2021%2003%3A21%3A05; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _dvs=0:kviry40e:JYV~ckjNr~aCqj1L7w_ITi2y~bzU36Cj; _userGUID=0:kvi1finn:FEigeIWNVY8qaoffb4T1Lj6UjQ7doGTi; AMWINE__AB_HASH=3_1; TEST_AMWINE__AB_HASH=undefined; AMWINE__IS_ADULT=Y; _hjid=1e77ce00-de83-41ab-b096-ea390c6b1c9d; _ym_d=1635854330; _ym_isad=2; _ym_uid=1635854330568852096; BX_USER_ID=0a16d9f004a897277adf34d9075b4890; dSesn=9b753f46-0d6b-bea7-013f-f85cf7a3d3ee; AMWINE__AUTO_GEOSERVICE=1; AMWINE__CITY_NAME=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; AMWINE__CITY_SALE_LOCATION_ID=19; AMWINE__REGION_CODE=moscow; AMWINE__REGION_ELEMENT_ID=342; AMWINE__REGION_ELEMENT_XML_ID=77; PHPSESSID=s1A8iSw2SUi0VtQCyo5iNez0I3WVsSVA',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'ru',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'amwine.middlewares.AmwineSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'amwine.middlewares.AmwineDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'amwine.pipelines.AmwinePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
