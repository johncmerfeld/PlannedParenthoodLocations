import scrapy

def get_urls():
    
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    states = [x.lower() for x in states]
    
    urls = []
    page1 = "https://www.plannedparenthood.org/health-center/"
    for state in states:
        s = page1 + state
        urls.append(s)
    return urls

class PlannedParenthoodScraper(scrapy.Spider):
    """
    This class first requests base urls, then from the base urls 
    we extract the next urls to call. We call all the possible urls
    and download the content from each one of them.
    """

    name = "ppscrapper"

    def start_requests(self):
        urls = get_urls()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.postParse)
    
    def postParse(self, response):
        
        base = "https://www.plannedparenthood.org"
        
        for link in response.xpath('*//a/@href').extract():
            if link.startswith("/health-center/"):
                yield {"link" : base + link}
            




