# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['princessinternational.ca']
    start_urls = ["https://princessinternational.ca/login.php"]

    # Authentication to login to the website - crendentials are removed for security     
    def parse(self, response):
        yield FormRequest('https://www.princessinternational.ca/login.php',
                            formdata ={ 'email':'**********************',
                                        'password':'*******',
                                        'Login':'Login',
                                        'process':'1'},
                            callback=self.parse_after_login)

    #After Authentication, site default page to order page. Prompt use to input the order they want to scrape
    def parse_after_login(self,response):
        if response.xpath('//*[@id="logout"]'):
            self.log('You logged in!')
        g = input('Enter Order ID to scrape:' )
        url = 'https://princessinternational.ca/inside/ordersDetails.php?storeOrderID=' + g
        self.log('URL to scrape: ' + url)
        yield scrapy.Request(url, callback=self.parse_page_listings)
      
    # Display the list of items that were ordered. Store the URL in a list and then recursively go to each product's URL to scrap
    def parse_page_listings(self,response):
        self.log('insice parse_page_listings')
        listing_url=response.xpath('//*[@class="reportTable"]//@href').extract()
        listing_url = list(dict.fromkeys(listing_url)) #remove url duplicates from listing_url
        print (listing_url)
        for item in listing_url:
            absolute_listing_url= response.urljoin(item)
            yield scrapy.Request(absolute_listing_url, callback=self.parse_individual_listings)

    #Paste the scraped data
    def parse_individual_listings(self,response):
        product_name=response.xpath('.//*[@style="width: 100%; text-align: left"]/text()').extract()
        product = response.xpath('.//*[@class="arial_black11"]/text()').extract()[2]
        price = response.xpath('.//*[@color="#FF0000"]/text()').extract()
        sku = response.xpath('.//*[@class="arial_black11"]/text()').extract()[1]
        image = response.css('img::attr(onclick)').extract()[-1]
        yield{'Product Name':product_name,'UPC': product,'Price':price,'Image':image, 'SKU':sku}