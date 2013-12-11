# Scrapy settings for BlogRipper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BlogRipper'

LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['BlogRipper.spiders']
NEWSPIDER_MODULE = 'BlogRipper.spiders'

FEED_EXPORTERS = {
    'html': 'BlogRipper.exporters.HtmlItemExporter',
}
