from BlogRipper.spiders import MicrosoftBlogSpider

class EriclippertMsdnSpider(MicrosoftBlogSpider):
    name = 'ericlippert_msdn'
    start_urls = ['http://blogs.msdn.com/b/ericlippert/']
    next_page_xpath = "//a[@class='selected']/following-sibling::a[@class='page']"