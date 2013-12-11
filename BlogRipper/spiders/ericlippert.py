from scrapy.contrib.loader import XPathItemLoader
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from BlogRipper.items import BlogripperItem
from BlogRipper.extractors import MySgmlLinkExtractor
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

class EriclippertSpider(BaseSpider):
    name = 'ericlippert'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    article_extractor = MySgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/')
    next_page_extractor = SgmlLinkExtractor(
                allow=r'/default.aspx\?PageIndex=\d+$', 
                restrict_xpaths="//a[@class='selected']/following-sibling::a[@class='page']")

    def parse(self, response):
        links = self.article_extractor.extract_links(response)  
        for l in links:
            yield BlogripperItem(l.text, l.url)            
        next_page = self.next_page_extractor.extract_links(response)[0]
        yield Request(next_page.url, callback=self.parse)
