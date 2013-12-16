from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as BuggySgmlLinkExtractor

class MySgmlLinkExtractor(BuggySgmlLinkExtractor):
    
    def __init__(self, allow, restrict_xpaths=()):
        BuggySgmlLinkExtractor.__init__(self, allow=allow, restrict_xpaths=restrict_xpaths)
        
    def unknown_endtag(self, tag):
        if self.scan_tag(tag):
            self.current_link = None    