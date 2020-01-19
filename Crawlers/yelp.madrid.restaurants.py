from google.cloud import storage
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import googlemaps

import scrapy
import json
import tempfile

gmaps = googlemaps.Client(API_KEY.api_key)
TEMPORARY_FILE = tempfile.NamedTemporaryFile(delete=False, mode='w+t')

def upload_file_to_bucket(bucket_name, blob_file, destination_file_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(blob_file.name, content_type='text/csv')
    
class YelpSpider(scrapy.Spider):
    name = 'yelpspider'
    cycles = 0
    ID = 1
    
    sites = "li.lemon--li__373c0__1r9wz"
    url = "div div div div div div div div div div div h3 span a::attr(href)"
    title = "div div div div div div div div div div div h3 span a::text"
    stars = "div.i-stars__373c0__Y2F3O::attr(aria-label)"
    reviews = "span.reviewCount__373c0__2r4xT::text"
    price = "span.priceRange__373c0__2DY87::text"
    category = "div div div div div div div div div div div span span span a::text"
    phone = "div div div div div div div div div div div p::text"
    address1 = "address div div div p span::text"
    address2 = "div div div div div div div div div div div div p::text"
    
    start_urls = ['https://www.yelp.es/search?cflt=restaurants&find_loc=Madrid%2C+Madrid%2C+ES']
    
    def parse(self, response):
        for site in response.css(self.sites):
            url_text = site.css(self.url).extract_first()
            title_text = site.css(self.title).extract_first()
            stars_number = site.css(self.stars).extract_first()
            reviews_number = site.css(self.reviews).extract_first()
            price_level = site.css(self.price).extract_first()
            category_text = site.css(self.category).extract_first()
            phone_text = site.css(self.phone).extract_first()
            address1_text = site.css(self.address1).extract_first()
            address2_text = site.css(self.address2).extract_first()
            
            if url_text and "/biz" not in url_text:
                url_text = None
                title_text = None
            else: url_text = f"https://www.yelp.es{url_text}"
            try: stars_number = float(stars_number.split(' ')[2])
            except: stars_number = None
            try: reviews_number = int(reviews_number.split(' ')[0])
            except: reviews_number = None
            if price_level and "€" not in price_level: price_level = None
            
            if None not in [url_text, title_text, stars_number, reviews_number, price_level, category_text, phone_text, address1_text, address2_text]:
                geocode_result = gmaps.geocode(address1_text + address2_text + " Madrid")
                if geocode_result and len(geocode_result) > 0:
                    lat = geocode_result[0]['geometry']['location']['lat']
                    lon = geocode_result[0]['geometry']['location']['lng']
                    TEMPORARY_FILE.writelines(f"{self.ID}||{url_text}||{title_text}||{stars_number}||{reviews_number}||{price_level}||{category_text}||{phone_text}||{address1_text}||{address2_text}||{lat}||{lon}\n")
                    self.ID += 1
                
        self.cycles += 1
            
        if self.cycles <= 10:
            yield response.follow(response.css('div.navigation-button-container__373c0__spUng a.next-link::attr(href)')[0], self.parse)
            
def activate(request):
    now = datetime.now()
    request_json = request.get_json()
    BUCKET_NAME = 'bda5-keepcoding-inot1'
    DESTINATION_FILE_NAME = 'datasets/yelp/food/' + now.strftime("%Y/%m/%d/") +'crawl.csv'
    TEMPORARY_FILE.writelines("ID||URL||Name||Score||Reviews||Price Level||Category||Phone||Address||District||Latitude||Longitude\n")
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(YelpSpider)
    process.start()
    TEMPORARY_FILE.seek(0)
    upload_file_to_bucket(BUCKET_NAME, TEMPORARY_FILE, DESTINATION_FILE_NAME)
    TEMPORARY_FILE.close()
    
    return "Sinvergüenza!"