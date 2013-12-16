# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.http import Request
from scrapy.spider import BaseSpider
from BlogRipper.items import ArticleItem

class BlogSpider(BaseSpider):
    def parse(self, response):
        articles = self.article_extractor.extract_links(response)  
        for link in articles:
            item = ArticleItem()      
            item['title'] = link.text
            item['url'] = link.url
            yield item
        next_pages = self.next_page_extractor.extract_links(response)
        if next_pages:
            yield Request(next_pages[0].url)