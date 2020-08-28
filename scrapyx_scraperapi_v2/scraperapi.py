# -*- coding: utf-8 -*-
__author__ = 'Henry B. <tubnd.younet@gmail.com>'

from scrapy.exceptions import NotConfigured

import logging

log = logging.getLogger('scrapyx.scraperapi')

class ScraperApiV2ProxyMiddleware(object):
    def __init__(self, settings):
        if not settings.getbool('SCRAPERAPI_ENABLED', True):
            raise NotConfigured
        
        self.SCRAPERAPI_URL = 'http://api.scraperapi.com/?url={url}&{params}'
        self.SCRAPERAPI_KEY = settings.get('SCRAPERAPI_KEY', '')
        self.SCRAPERAPI_RENDER = settings.get('SCRAPERAPI_RENDER', False)
        self.SCRAPERAPI_PREMIUM = settings.get('SCRAPERAPI_PREMIUM', False)
        self.SCRAPERAPI_COUNTRY_CODE = settings.get('SCRAPERAPI_COUNTRY_CODE', '')

        self.url_params = ''
        params = []
        params.append('api_key={}'.format(self.SCRAPERAPI_KEY))
        if self.SCRAPERAPI_RENDER:
            params.append('render=true')

        if self.SCRAPERAPI_PREMIUM:
            params.append('premium=true')

        if self.SCRAPERAPI_COUNTRY_CODE:
            params.append('country_code={}'.format(self.SCRAPERAPI_COUNTRY_CODE))

        if len(params):
            self.url_params = '&'.join(params)        

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def process_request(self, request, spider):
        log.info("Process request...")        

        new_url = self.SCRAPERAPI_URL.format(url=request.url, params=self.url_params)
        
        log.info("New url: {}".format(new_url))
        request.replace(url=new_url)