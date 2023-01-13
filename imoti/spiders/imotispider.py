import scrapy

class ImotispiderSpider(scrapy.Spider):
    name = 'imot'
    allowed_domains = ['imoti.bg']
    start_urls = ['https://imoti.bg/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B1%D0%B8']

    def parse(self, response):
        products = response.css('div.col-md-6.col-lg-4')[:-2]
        for product in products:
            yield {
                'type': product.css('a::text').get(),
                'price': product.css('span::text').get(),
                'size': product.css('li span:nth-of-type(2)::text').get(),
                'location': product.css('div.btext::text').get(),
                'realtor': product.css('span.agency::text').get() or 'Private Sale',
                'link': product.css('a').attrib['href'],
            }

        options = response.css("select#pagination option")
        for option in options:
            url = option.css("option::attr(value)").get()
            yield scrapy.Request(url, callback=self.parse)
