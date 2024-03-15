import selenium
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from config import BROWSER_SERVICE


# class Browser:
#     service =''
#     def __init__(self):
#         self.service = wd.Firefox

#     def myconnect(self):
#         return self.service
#     # def get(self):
#     #     return self.service


class WebElement:

    # is_found = False
    # content = []
    # num_items = -1
    # service = ''
    # name = ''
    # url = ''

    def __init__(self, item, obj):
        # self.page_content = page_content
        # self.url = url
        # self.service = service
        self.element = ''
        self.item = item
        self.source_object = obj
        self.element = self.__get()



    def __get(self):
        self.element = self.source_object.find_element_by_class_name(self.item)
        return self.element



    # def get_tag_content(self, name):
    #     """Return First Item"""
    #     self.item = self.service().find_elements_by_tag_name(name)
    #     self.item = 1
    #     return [self.item]


    # def find_all(self, name):
    #     """Return List of All Items"""
    #     item = ''
    #     return [item]



class WebPage:

# Class variables
    WAIT_TIME = 10
    # is_browser_connected = False
    # browser = webdriver.Firefox()
    # url = ''
    # page = ''
    # content = ''

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



# pg = WebPage("https://docs.couchbase.com/home/mobile.html",True)
# el = WebElement("menu_row", pg.browser)

# print(el)