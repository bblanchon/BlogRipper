from BlogRipper.spiders import BlogSpider

class HanselmanSpider(BlogSpider):
    name = 'hanselman'
    start_urls = ['http://www.hanselman.com/blog/']
    article_xpath = "//h2/a"
    next_page_xpath = "//div[@class='paging-prev']/a"