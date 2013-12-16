from BlogRipper.spiders import MicrosoftBlogSpider

class JonskeetSpider(MicrosoftBlogSpider):
    name = 'jonskeet'
    start_urls = ['http://msmvps.com/blogs/jon_skeet/']
    article_xpath = "//h2/a"
    next_page_xpath = "//a[starts-with(text(),'Next')]"