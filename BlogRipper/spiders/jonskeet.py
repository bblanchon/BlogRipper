from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from BlogRipper.spiders import BlogSpider
from BlogRipper.extractors import MySgmlLinkExtractor

class JonskeetSpider(BlogSpider):
    name = 'jonskeet'
    allowed_domains = ['msmvps.com']
    start_urls = ['http://msmvps.com/blogs/jon_skeet/']
    article_extractor = MySgmlLinkExtractor(allow=r'/archive/\d{4}/\d{2}/\d{2}/[^#]+$', restrict_xpaths="//h2/a")
    next_page_extractor = SgmlLinkExtractor(allow=r'/default.aspx\?PageIndex=\d+$', restrict_xpaths="//a[starts-with(text(),'Next')]")