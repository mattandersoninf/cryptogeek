# Main scraping class file:

# requests and beautifulsoup4 are ideal for grabbing data from static webpages
import requests
from bs4 import BeautifulSoup as soup

# to be used for organizing the information scraped into a csv file
# import csv

# for printing to analyze
from pprint import pprint

# web automation library
from selenium import webdriver


cryptoCompareUrl = 'https://www.cryptocompare.com/'

"""
class mainScraper(self,siteList):
    
    for site in siteList:
        
"""


"""
def getWebpage(url):
    
    # get google Chrome webdriver
    browser = webdriver.Chrome()
    browser.get(url)
"""    
    

def getCryptoCompareSoup():
    
    # get google Chrome webdriver
    browser = webdriver.Chrome()
    browser.get(cryptoCompareUrl)
    
    # request the cryptocompare webpage
    cryptoCompareHtml = browser.execute_script("return document.documentElement.innerHTML;") 
    
    """
    # requests.get(cryptoCompareUrl)
    
    #cryptoCompareHtml = browser.page_source
    
    #BeautifulSoup(cryptoCompareRequest, '')
    """
    
    # close chrome browser that you opened with selenium
    browser.close()
    
    # return the innerhtml of the web page
    return cryptoCompareHtml




# function to scrape cryptocurrency information from  https://www.cryptocompare.com/
#def scrapeCryptoCompare():
    
    #form the 


if __name__=="__main__":
    
    pprint(getCryptoCompareSoup())