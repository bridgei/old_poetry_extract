from helpers import WebPage
from bs4 import BeautifulSoup as bs4

class HtmlObject(object):

  def __init__(self, content, parser=bs4):
    self.content =  parser(content, 'html.parser')
    self.is_found = len(content)>0

  def find_all_by_tag(self, search):
    return self.content.find_all(search)

  def find_all_by_class(self, search):
    return self.content.find_all(class_=search)


  def find_by_tag(self, search):
    return self.content.find(search)

  def find_by_class(self, search):
    return self.content.find(class_=search)
