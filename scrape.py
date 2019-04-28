# Main scraping class file:

# requests and beautifulsoup4 are ideal for grabbing data from static webpages
import requests

# grabbing static html
from bs4 import BeautifulSoup as soup

# to be used for organizing the information scraped into a csv file
import csv

# use pandas for storing information in a dataframe
# you can throw it directly into files but in case you want to structure
# the information as you get it and throw it between documents or databases
# this is convenient
# more likely to use because of previous experience with matplotlib and jupyter nb
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


from datetime import datetime


cryptoCompareUrl = 'https://www.cryptocompare.com/coins/list/USD/1'

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
def scrapeCryptoCompare():
    
    # get google Chrome webdriver
    with webdriver.Chrome() as driver:
        
        # give the driver 30 seconds to open up the browser
        driver.implicitly_wait(30)
        
        # open up cryptocompare
        driver.get(cryptoCompareUrl)
        
        # give selenium page source to beautifulsoup
        cryptoCompareSoup = soup(driver.page_source,'html.parser')
        """
        # soup element - place - text
        cryptoName = [item.text.strip() for item in cryptoCompareSoup.find_all('span',{'class':'mobile-name ng-binding'})]
        
        cryptoPrice = [item.text.strip() for item in cryptoCompareSoup.find_all('div', {'class':['current-price-value ng-binding','current-price-value ng-binding highlight-down value-down','current-price-value ng-binding highlight-up value-up']})]
        
        cryptoVolume =[item.text.strip() for item in cryptoCompareSoup.find_all('td',{'class':'full-volume col-selected'})]
        
        # in case this line does not work, try this to make the findChild function more specific to the class a
        
        crypto24HrDelta = [item.findChild('span').text.strip() for item in cryptoCompareSoup.find_all('td',{'ng-class':["{'col-selected':tableColumns[6].sortApplied}"]})]    
        """
        
        cryptoCompareDataFrame = pd.DataFrame({'Name':[item.text.strip() for item in cryptoCompareSoup.find_all('span',{'class':'mobile-name ng-binding'})],
                                               'Price':[item.text.strip() for item in cryptoCompareSoup.find_all('div', {'class':['current-price-value ng-binding','current-price-value ng-binding highlight-down value-down','current-price-value ng-binding highlight-up value-up']})],
                                               'Volume':[item.text.strip() for item in cryptoCompareSoup.find_all('td',{'class':'full-volume col-selected'})],
                                               '24HrDelta':[item.findChild('span').text.strip() for item in cryptoCompareSoup.find_all('td',{'ng-class':["{'col-selected':tableColumns[6].sortApplied}"]})],
                                               'Time':f"{datetime.now(): %Y-%m-%d %H:%M:%S}"})
                
        cryptoCompareDataFrame.to_csv('crypto_currency.csv', index = False, mode ='a', header = False)
    
        """
        # if the file does not exist in your current directory, it wil be made
        # else open it in your current directory
        # 'wb' = writeback
        with open('crypto_currency.csv', 'wb') as csvfile:
            
            # create csv writing obj
            csvwriter = csv.writer(csvfile)
        """
        
        """
        # by wrapping these line in a "with" statement,
        # the driver will close automatically after scraping the site
        # close chrome browswer that you opened with selenium
        driver.close()
        """
        

# function to scrape cryptocurrency information from  https://www.cryptocompare.com/
#def scrapeCryptoCompare():
    
    #form the 


if __name__=="__main__":
    
    scrapeCryptoCompare()