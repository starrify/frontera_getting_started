#coding: utf8

import urlparse

import scrapy


class TestingSpider(scrapy.Spider):
    name = "testing"
    #allowed_domains = ["scrapinghub.com"]
    start_urls = (
        'http://scrapinghub.com/',
    )

    def parse(self, response):
        if not isinstance(response, scrapy.http.TextResponse):
            return
        for href in response.css(
                'a::attr(href),'
                'a::attr(data-href),'
                'frame::attr(src),'
                'iframe::attr(src)'
            ).extract():
            url = urlparse.urljoin(response.url, href).lower()
            yield scrapy.Request(
                url=url,
                meta={
                    # Shorter first ;)
                    'score': -1 * len(url),
                }
            )
