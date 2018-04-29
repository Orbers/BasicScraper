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
os.environ["webdriver.chrome.driver"] = chromedriver


# Opens a Chrome window and goes to google.com
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.expedia.com/')

# Waits 1 second for the page to load and then goes to the search box
time.sleep(1);

origin = driver.find_element_by_id("package-origin-hp-package")
origin.send_keys("ORD")
origin.send_keys(Keys.RETURN)

time.sleep(1);

destination = driver.find_element_by_id("package-destination-hp-package")
destination.send_keys("DUR-King Shaka Intl.")
destination.send_keys(Keys.RETURN)

time.sleep(1)

departing = driver.find_element_by_id("package-departing-hp-package")
departing.send_keys("10/17/2018")
departing.send_keys(Keys.RETURN)


returning = driver.find_element_by_id("package-returning-hp-package")
returning.send_keys("10/18/2018")
returning.send_keys(Keys.RETURN)

searchButton = driver.find_element_by_id('search-button-hp-package')