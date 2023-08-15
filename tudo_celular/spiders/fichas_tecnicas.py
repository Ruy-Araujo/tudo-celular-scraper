import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader

from tudo_celular.items.smartphone import SmartphoneItem


class FichasTecnicasSpider(scrapy.Spider):
    name = "fichas_tecnicas"
    allowed_domains = ["www.tudocelular.com"]
    url = "https://www.tudocelular.com"
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=f"{self.url}/celulares/fichas-tecnicas.html", callback=self.parse)

    def parse(self, response):
        if response.status == 302:
            raise CloseSpider("No more pages scrapy will be closed...")

        for phone in response.xpath('//article[@class="phonelist_item"]'):
            item = ItemLoader(item=SmartphoneItem())
            item.add_value('Brand', phone.xpath('div[2]/a/h4/strong/text()').get())
            item.add_value('Model', phone.xpath('div[2]/a/h4/text()').get())
            item.add_value('Image', phone.css('img').attrib['style'])
            item.add_value('Score', phone.xpath('div[1]/div/strong/text()').get())
            item.add_value('Price', phone.xpath('div[2]/div/a[1]/span[2]/text()').get())
            item.add_value('Url', self.url + phone.xpath('a[@class="pic"]').attrib['href'])

            yield item.load_item()

        # Paginate
        # self.page += 1
        # next_page = f"{self.url}/celulares/fichas-tecnicas_{self.page}.html"
        # yield response.follow(url=next_page, callback=self.parse)
