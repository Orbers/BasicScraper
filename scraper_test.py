from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import time
import os

config = ConfigParser()
config.read('config.ini') # Reads your local environ variables from a config.ini file

"""
The following code will set up the chromedriver filepath by pulling the
    filepath variable from your local config.ini file. 
    This file should be in the root of the project directory.
"""

chromedriver = config.get('LocalEnvironment', 'chrome_path')
print("chromdriver = " + chromedriver)
os.environ["webdriver.chrome.driver"] = chromedriver


# Opens a Chrome window and goes to google.com
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.southwest.com/flight/shortcut/low-fare-search.html?int=HOME-BOOKING-WIDGET-ADVANCED-AIR')

# Waits 1 second for the page to load and then goes to the search box
time.sleep(1);

origin = driver.find_element_by_id("originAirport_displayed")
origin.send_keys("mdw")
origin.send_keys(Keys.RETURN)

time.sleep(1);

destination = driver.find_element_by_id("destinationAirport_displayed")
destination.send_keys("pdx")
destination.send_keys(Keys.RETURN)

time.sleep(1)

departing = driver.find_element_by_id("outboundDate")
departing.send_keys("oct")
departing.send_keys(Keys.RETURN)

time.sleep(1)

returning = driver.find_element_by_id("returnDate")
#returning.clear()
returning.send_keys("oct")
returning.send_keys(Keys.RETURN)

searchButton = driver.find_element_by_id('submitButton').click()