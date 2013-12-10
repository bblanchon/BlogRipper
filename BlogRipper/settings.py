# Scrapy settings for BlogRipper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BlogRipper'

SPIDER_MODULES = ['BlogRipper.spiders']
NEWSPIDER_MODULE = 'BlogRipper.spiders'

FEED_EXPORTERS = {
    'md': 'BlogRipper.exporters.MarkdownItemExporter',
}
