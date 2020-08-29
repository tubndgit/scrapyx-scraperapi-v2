# scrapyx-scraperapi-proxy

Scraper API middleware for Scrapy (http://scrapy.org/)
=======================================================

Processes Scrapy requests a man in the middle proxy service using https://www.scraperapi.com


Required
--------

    python version >= 2.7


Install
--------

Checkout the source and run

    python setup.py install

Or

    pip install scrapyx-scraperapi-v2
    

settings.py
-----------

    # Activate the middleware
    SCRAPERAPI_ENABLED = True
    
    # The API key 
    SCRAPERAPI_KEY='your API key'

    # JS Redering 
    SCRAPERAPI_RENDER = False

    # Premium account
    SCRAPERAPI_PREMIUM = False

    # Geographic Location
    # 'US', 'UK', ...
    SCRAPERAPI_COUNTRY_CODE = ''

    DOWNLOADER_MIDDLEWARES = {
        'scrapyx_scraperapi_v2.ScraperApiV2ProxyMiddleware': 610,
    }


