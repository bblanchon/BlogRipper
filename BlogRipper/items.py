from scrapy.item import Item, Field

class BlogripperItem(Item):
    title = Field()
    url = Field()
