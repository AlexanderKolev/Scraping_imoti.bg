# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImotiItem(scrapy.Item):
    type = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    location = scrapy.Field()
    realtor = scrapy.Field()
    link = scrapy.Field()
