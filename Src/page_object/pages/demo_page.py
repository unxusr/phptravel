import sys
import os
from selenium.webdriver.common.by import By
from Src.page_object.locators import Locator

class DemoHomePage(object):
    def __init__(self, driver):
        self.driver = driver
