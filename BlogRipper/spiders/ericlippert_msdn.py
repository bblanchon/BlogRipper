from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from BlogRipper.spiders import BlogSpider
from BlogRipper.extractors import MySgmlLinkExtractor

class EriclippertMsdnSpider(BlogSpider):
    name = 'ericlippert_msdn'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    article_extractor = MySgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/')
    next_page_extractor = SgmlLinkExtractor(
                allow=r'/default.aspx\?PageIndex=\d+$', 
                restrict_xpaths="//a[@class='selected']/following-sibling::a[@class='page']")