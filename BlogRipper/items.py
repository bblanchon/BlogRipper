from scrapy.item import Item, Field

class BlogripperItem(Item):
    title = Field()
    url = Field()
    
    def __init__(self, title, url):
        Item.__init__(self)
        self['title'] = title
        self['url'] = url
