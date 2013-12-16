from BlogRipper.spiders import BlogSpider

class EriclippertMsdnSpider(BlogSpider):
    name = 'ericlippert_msdn'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    article_regex = r'/archive/\d{4}/\d{2}/\d{2}/'
    next_page_regex = r'/default.aspx\?PageIndex=\d+$'
    next_page_xpath = "//a[@class='selected']/following-sibling::a[@class='page']"