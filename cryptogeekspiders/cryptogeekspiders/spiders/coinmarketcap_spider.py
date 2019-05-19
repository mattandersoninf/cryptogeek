
import scrapy

import os

filename = 'coinmarketcap_data.csv'

class CoinMarketSpider(scrapy.Spider):

    name = "coinmarketcap"

    start_urls = ['https://coinmarketcap.com/all/views/all/']

    fields = ['Name']

    """
    response = HtmlResponse(url=coinMarketCapUrl)

    selector = Selector(response=response)
    """

    def parse(self, response):

        # self.logger.info('A response from %s just arrived!', response.url)

        # filename = 'data/coinmarketcap_data.csv'

        
        #for tablerow in response.xpath("//tr[contains(@role,'row')]"):
        
        cryptoName = response.xpath('//td[@class="text-left col-symbol"]/text()').extract()
        
        yield{
            'Name': cryptoName.text
        }
        

        # this works but this just puts the whole html into the csv, not very specific
        """
        with open(filename, 'wb') as f:
            f.write(response.body)
        """