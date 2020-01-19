# Script para probar que mi crawler va por buen camino antes de desplegarlo como Cloud Function.

from scrapy.crawler import CrawlerProcess
import scrapy

class YelpSpider(scrapy.Spider):
    name = 'yelpspider'
    
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
    
    # Podeis cambiar la url inicial por otra u otras paginas
    start_urls = ['https://www.yelp.es/search?cflt=restaurants&find_loc=Madrid%2C+Madrid%2C+ES']
    
    # Aqui scrapeamos los datos y los imprimimos a un fichero
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
              
            # Print a un fichero
            if None not in [url_text, title_text, stars_number, reviews_number, price_level, category_text, phone_text, address1_text, address2_text]:
                print(f"{url_text}||{title_text}||{stars_number}||{reviews_number}||{price_level}||{category_text}||{phone_text}||{address1_text}||{address2_text}")
            
        
        
        # Aqui hacemos crawling (con el follow)
        yield response.follow(response.css('div.navigation-button-container__373c0__spUng a.next-link::attr(href)')[0], self.parse)
            
process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
process.crawl(YelpSpider)
process.start()