from scrapy.spider import BaseSpider
from BlogRipper.items import BlogripperItem
from scrapy.http import Request
from BlogRipper.extractors import SgmlLinkExtractor

class EriclippertSpider(BaseSpider):
    name = 'ericlippert'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    link_extractor = SgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/')
    page_index = 0

    def parse(self, response):
        links = self.link_extractor.extract_links(response)  
        for l in links:
            yield BlogripperItem(l.text, l.url)            
        self.page_index += 1;
        url = "http://blogs.msdn.com/b/ericlippert/default.aspx?PageIndex=%d" % self.page_index
        yield Request(url, callback=self.parse)
