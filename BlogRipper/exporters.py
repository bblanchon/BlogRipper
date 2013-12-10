from scrapy.contrib.exporter import BaseItemExporter

class HtmlItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file

    def start_exporting(self):
        self.file.write("<html><body><ol>")

    def finish_exporting(self):
        self.file.write("</ol></body></html>")
        
    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        self.file.write(u"<li><a href='%s'>%s</a></li>\n" % (item['url'], item['title']))