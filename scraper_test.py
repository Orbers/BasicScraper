from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chromedriver = "/Applications/chromedriver"
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
departing.send_keys("01/12/2020")
departing.send_keys(Keys.RETURN)
