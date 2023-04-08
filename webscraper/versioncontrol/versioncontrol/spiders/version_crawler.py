from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "v_crawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

#setting proxy server  that will prevent us from getting 
# banned by the website for making many requests at a great speed 
# this thing just set a proxy server that will make requests on our behalf 
#by changing our ip with multiple different ip

    PROXY_SERVER = "ip address of proxy server"

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"),callback="parse_item")
    )

    def parse_item(self, response):
        yield {
            "title" : response.css(".product_main h1::text").get(),
            "price" : response.css(".price_color::text").get(),
            "availability" : response.css(".availability::text")[1].get().replace("\n","").replace(" ","")
        }