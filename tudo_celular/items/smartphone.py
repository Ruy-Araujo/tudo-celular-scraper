from datetime import datetime
from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


class SmartphoneItem(Item):
    Brand = Field(output_processor=TakeFirst())
    Model = Field(output_processor=TakeFirst())
    Image = Field(output_processor=TakeFirst())
    Score = Field(output_processor=TakeFirst())
    Price = Field(output_processor=TakeFirst())
    Details_url = Field(output_processor=TakeFirst())
    Extracted_at = datetime.now().isoformat()
