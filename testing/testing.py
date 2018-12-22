'''
Created on Dec 22, 2018

@author: APPLE
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

user = "9362077226"
pwd = "yoyo7466"
'''driver = webdriver.Firefox(executable_path='/Users/APPLE/Downloads/geckodriver')
driver = webdriver.Chrome(executable_path='/Users/APPLE/Downloads/chromedriver')
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
time.sleep(10)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
time.sleep(10)
elem.send_keys(Keys.RETURN)
time.sleep(10)
driver.close()'''
website = webdriver.Chrome(executable_path='/Users/APPLE/Downloads/chromedriver')
website.get("https://www.wikipedia.org")
assert "Wikipedia" in website.title
elem = website.find_element_by_id("js-link-box-en")
elem.click();
time.sleep(10)
assert "Wikipedia, the free encyclopedia" in website.title
website.close()