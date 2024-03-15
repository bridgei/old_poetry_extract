import selenium
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class WebElement:

    def __init__(self, item, obj):
        self.element = ''
        self.item = item
        self.source_object = obj
        self.element = self.__get()


    def __get(self):
        self.element = self.source_object.find_element_by_class_name(self.item)
        return self.element

class WebPage:

    WAIT_TIME = 10

    def __init__(self, url, keep_open = False):
        self.browser = webdriver.Firefox()
        self.url = url
        self.page = ''
        self.is_browser_connected = self.browser.name == 'firefox'
        if self.is_browser_connected:
          self.content = self.__get()
        if keep_open is False:
          self.browser.close()
          self.is_browser_connected = self.browser.name == 'firefox'


    def __get(self):
        self.browser.get(self.url)
        time.sleep(self.WAIT_TIME)
        self.content = self.browser.page_source
        return self.content

