from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as BuggySgmlLinkExtractor

class SgmlLinkExtractor(BuggySgmlLinkExtractor):
    
    def __init__(self, allow):
        BuggySgmlLinkExtractor.__init__(self, allow=allow)
        
    def unknown_endtag(self, tag):
        if self.scan_tag(tag):
            self.current_link = None    