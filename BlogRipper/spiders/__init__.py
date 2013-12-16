# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from scrapy.http import Request
from scrapy.spider import BaseSpider
from BlogRipper.extractors import MySgmlLinkExtractor
from BlogRipper.items import ArticleItem

class BlogSpider(BaseSpider):

    article_regex = ()
    article_xpath = ()
    next_page_regex = ()
    next_page_xpath = ()

    def __init__(self, *a, **kw):
        super(BaseSpider, self).__init__(*a, **kw)
        self.article_extractor = MySgmlLinkExtractor(allow=self.article_regex, restrict_xpaths=self.article_xpath)
        self.next_page_extractor = SgmlLinkExtractor(allow=self.next_page_regex, restrict_xpaths=self.next_page_xpath)

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