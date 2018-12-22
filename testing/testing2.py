'''
Created on Dec 22, 2018

@author: APPLE
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/APPLE/Downloads/chromedriver')

    def test_search_in_python_org(self):
        user = "s1000747@mail.yzu.edu.tw"
        pwd = "yoyo1221"
        driver = self.driver
        driver.get("http://www.facebook.com")
        self.assertIn("Facebook", driver.title)
        elem = driver.find_element_by_id("email")
        elem.send_keys(user)
        time.sleep(5)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        #time.sleep(5)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()