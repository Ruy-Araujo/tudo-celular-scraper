import re

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


def parse_image(value):
    pattern = r"(?<=')(.*?)(?=\?)"
    return re.findall(pattern, value)


def parse_preco(value):
    if "Aviso de preço" in value:
        return None
    else:
        return value


class SmartphoneItem(Item):
    Brand = Field(output_processor=TakeFirst())
    Model = Field(output_processor=TakeFirst())
    Image = Field(input_processor=MapCompose(parse_image), output_processor=TakeFirst())
    Score = Field(output_processor=TakeFirst())
    Price = Field(input_processor=MapCompose(parse_preco), output_processor=TakeFirst())
    Url = Field(output_processor=TakeFirst())
    Details = Field(output_processor=TakeFirst())
    Extracted_at = Field(output_processor=TakeFirst())
