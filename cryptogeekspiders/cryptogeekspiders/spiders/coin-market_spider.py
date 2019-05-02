


import scrapy


coinMarketCapUrl = 'https://coinmarketcap.com/all/views/all/'


class CoinMarketSpider(scrapy.Spider):

    name = "coin-market"

    start_urls = [coinMarketCapUrl]

    """
    response = HtmlResponse(url=coinMarketCapUrl)

    selector = Selector(response=response)
    """

    def start_requests(self):
        urls = [coinMarketCapUrl]
        for url in urls:
            yield scrapy.Request(url=url,callback = self.parse())

    def parse(self, response):
        for tablerow in response.xpath("'//tr[contains(@role,'row')]"):
            yield{
                'Name': tablerow.xpath("td[contains(@class,'text-left col-symbol')]/text()".get())
            }

