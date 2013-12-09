from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from BlogRipper.items import BlogripperItem
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

class MySgmlLinkExtractor(SgmlLinkExtractor):
    
    def __init__(self, allow):
        SgmlLinkExtractor.__init__(self, allow=allow)
        
    def unknown_endtag(self, tag):
        if self.scan_tag(tag):
            self.current_link = None    

class EriclippertSpider(CrawlSpider):
    name = 'ericlippert'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    link_extractor = MySgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/')

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/default.aspx\?PageIndex=\d+')),
    )

    def parse(self, response):
        CrawlSpider.parse(self, response)
        links = self.link_extractor.extract_links(response)        
        return [ BlogripperItem(l.text, l.url) for l in links ]
