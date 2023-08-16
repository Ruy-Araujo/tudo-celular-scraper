import scrapy
from datetime import datetime
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
            item.add_value('Extracted_at', datetime.now().isoformat())

            # Phone details
            details_url = self.url + phone.xpath('a[@class="pic"]').attrib['href']
            yield scrapy.Request(details_url, callback=self.parse_details, meta={'item': item})

        # Paginate
        self.page += 1
        next_page = f"{self.url}/celulares/fichas-tecnicas_{self.page}.html"
        yield response.follow(url=next_page, callback=self.parse)

    def parse_details(self, response):
        item = response.meta['item']
        details = {}
        sections = response.xpath('//div[@class="row_titles"]/h3/strong/text()').getall()
        sections.insert(0, "BÁSICO")
        titles = response.xpath('//div[@class="row_titles"]/ul[@class="phone_column_features"]')
        values = response.xpath('//div[@class="phone_column"]/ul[@class="phone_column_features"]')

        # Block to handle values
        for i in range(len(sections)):
            details[sections[i]] = {}
            # Block to handle values that have <i> and <b> tags
            for title, value in zip(titles[i].xpath('li'), values[i].xpath('li')):
                v = ''
                # Handle icon
                if value.xpath('i[@class]'):
                    v = value.xpath('i[@class]').attrib['class'] + ' '
                # Handle bold
                elif value.xpath('b/text()'):
                    v += value.xpath('b/text()').get() + ' '
                # Handle price
                elif value.xpath('a/b/text()'):
                    v += value.xpath('a/b/text()').get() + ' '

                # Handle text
                if value.xpath('text()'):
                    v += value.xpath('text()').get()

                details[sections[i]].update({
                    title.xpath('text()').get(): v
                })

        item.add_value('Details', details)
        yield item.load_item()
