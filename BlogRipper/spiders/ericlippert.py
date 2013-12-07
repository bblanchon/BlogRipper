from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from BlogRipper.items import BlogripperItem
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

class EriclippertSpider(CrawlSpider):
    name = 'ericlippert'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/'), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=r'/default.aspx\?PageIndex=\d+'), callback='parse'),
    )

    def parse_item(self, response):
        l = XPathItemLoader(BlogripperItem(), response=response)
        l.add_value('url', response.url)
        l.default_input_processor = MapCompose(unicode.strip)
        l.default_output_processor = TakeFirst()
        l.add_xpath('title', "/html/head/title/text()")
        return l.load_item() 
