from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from BlogRipper.items import BlogripperItem
from BlogRipper.extractors import MySgmlLinkExtractor
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

class EriclippertSpider(CrawlSpider):
    name = 'ericlippert'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    link_extractor = MySgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/')

    rules = (
        Rule(SgmlLinkExtractor(
                allow=r'/default.aspx\?PageIndex=\d+$', 
                restrict_xpaths="//a[@class='selected']/following-sibling::a[@class='page']"), 
            follow=True, callback='parse_page'),
    )

    def parse_page(self, response):
        links = self.link_extractor.extract_links(response)        
        return [ BlogripperItem(l.text, l.url) for l in links ]
