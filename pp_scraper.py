import scrapy, json

# read from the list of URLS generated previously
def get_urls():
    file = "health_centers.json"
    urls = []
    with open(file) as f:
        links = json.load(f)
    for i in range(len(links)):
        link = links[i]["link"]
        urls.append(link)
    return urls

class PlannedParenthoodScraper(scrapy.Spider):
    """
    This class first requests base urls, then from the base urls 
    we extract the next urls to call. We call all the possible urls
    and download the content from each one of them.
    """

    name = "pp_address_scrapper"

    def start_requests(self):
        urls = get_urls()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for post in response.xpath('//p[@class="address-loc"]'):
            
            address = post.xpath('//span[@itemprop="streetAddress"]/text()').get()
            locality = post.xpath('//span[@itemprop="addressLocality"]/text()').get()
            region = post.xpath('//span[@itemprop="addressRegion"]/text()').get()
            postal = post.xpath('//span[@itemprop="postalCode"]/text()').get()
            
            yield {"address" : address,
                   "locality": locality,
                   "region"  : region,
                   "postal"  : postal} 
            


with open("addresses.json") as f:
    data = json.load(f)

import csv
with open('health_centers.csv', 'w', newline='') as csvfile:
    fieldnames = ["address", "locality", "region", "postal"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
