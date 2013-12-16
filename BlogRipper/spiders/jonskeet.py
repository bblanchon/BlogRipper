from BlogRipper.spiders import BlogSpider

class JonskeetSpider(BlogSpider):
    name = 'jonskeet'
    allowed_domains = ['msmvps.com']
    start_urls = ['http://msmvps.com/blogs/jon_skeet/']
    article_regex = r'/archive/\d{4}/\d{2}/\d{2}/[^#]+$'
    article_xpath = "//h2/a"
    next_page_regex = r'/default.aspx\?PageIndex=\d+$'
    next_page_xpath = "//a[starts-with(text(),'Next')]"