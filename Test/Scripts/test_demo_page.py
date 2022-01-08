from Src.test_base.web_driver_setup import WebDriverSetup
import unittest
from selenium import webdriver

class PHPTravelDemoHomePage(WebDriverSetup):

    def test_demo_page(self):
        self.driver.get('https://phptravels.com/demo/')
        self.driver.set_page_load_timeout(30)
        page_title = 'Demo Script Test drive - PHPTRAVELS'

        try:
            if self.driver.title == page_title:
                self.assertEqual(self.driver.title,page_title)
                print("Web page loaded successfully!")

        except Exception as error:
            print(error + "PHPTravel NOT LOADED")

if __name__ == '__main__':
    unittest.main()
