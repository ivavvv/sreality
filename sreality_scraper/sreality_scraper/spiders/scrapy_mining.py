import time
import json
import scrapy

class Sreality_Spider(scrapy.Spider):
    # time from 1.1.1970
    sec = str(time.time()*1000)
    sec = sec.split('.')[0]


    name = "sreality"
    start_urls = [f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&tms={sec}',]
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    }

    def parse(self, response):
        data = json.loads(response.body)
        for estate in data['_embedded']['estates']:

            name = estate.get('name')
            images = [img.get('href') for img in estate.get('_links', {}).get('images', [])]

            # Get the first image if available
            first_image = images[0] if images else None

            if name and first_image:
                yield {'name': name, 'images': first_image}