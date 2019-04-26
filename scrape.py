# Main scraping class file:

# requests and beautifulsoup4 are ideal for grabbing data from static webpages
import requests

# grabbing static html
from bs4 import BeautifulSoup as soup

# to be used for organizing the information scraped into a csv file
# import csv

# use pandas for storing information in a dataframe
# you can throw it directly into files but in case you want to structure
# the information as you get it and throw it between documents or databases
# this is convenient
import pandas as pd

# collections is another library for making datastructures to pass around data
# use which ever you choose

import collections as c


# for printing to analyze
from pprint import pprint

# web automation library, grabbign dynamic web pages
from selenium import webdriver

# construct regular expressions
import re


cryptoCompareUrl = 'https://www.cryptocompare.com/'

"""
class mainScraper(self,siteList):
    
    for site in siteList:
        
"""


"""
def getWebpage(url):
    
    # get google Chrome webdriver
    driver = webdriver.Chrome()
    driver.get(url)
"""    
    

# function to scrape cryptocompare.com
def getCryptoCompareSoup():
    
    # get google Chrome webdriver
    with webdriver.Chrome() as driver:
        
        # give the driver 3o seconds to open up the browser
        driver.implicitly_wait(30)
        
        # open up cryptocompare
        driver.get(cryptoCompareUrl)
        
        # give sleenium page source to beautifulsoup
        cryptoCompareSoup = soup(driver.page_source,'html.parser')
        
        pprint(cryptoCompareSoup.find_all('span',{'class':'mobile-name ng-binding'}))
        
        """
        # request the cryptocompare html
        cryptoCompareHtml = driver.execute_script("return document.documentElement.innerHTML;") 
        """
        
        """
        # form a defaultdict to grab information from the 
        crytoCompareDict = c.defaultdict(dict)
        """
        
        
        """
        # requests.get(cryptoCompareUrl)
        
        #cryptoCompareHtml = driver.page_source
        
        #BeautifulSoup(cryptoCompareRequest, '')
        """
        
        """
        # by wrapping these line in a "with" statement,
        # the driver will close automatically after scraping the site
        # close chrome browswer that you opened with selenium
        driver.close()
        """
        
        """
        # return the innerhtml of the web page
        return cryptoCompareHtml
        """

# function to scrape cryptocurrency information from  https://www.cryptocompare.com/
#def scrapeCryptoCompare():
    
    #form the 


if __name__=="__main__":
    
    pprint(getCryptoCompareSoup())