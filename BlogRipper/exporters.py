from scrapy.contrib.exporter import BaseItemExporter

class MarkdownItemExporter(BaseItemExporter):
    
    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.count = 0
        
    def export_item(self, item):
        self.count += 1
        self.file.write("%d. [%s](%s)\n" % (self.count, item['title'].encode('utf-8'), item['url']))