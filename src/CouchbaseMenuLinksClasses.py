
from WebObjectClasses import WebPage
from HtmlObjectClasses import HtmlObject
from validURL import is_ValidUrl

class CouchbaseMenuLinks:

  def __init__(self, url):
    # get html content from page
    self.menu_item_list = []
    self.component_list = []
    self.url = url
    self.html =  HtmlObject(WebPage(self.url).content)
    self.component_list = self.__get_component_list(self.html)
    self.menu_item_list = self.__build_menu_item_list(self.html)


  def __get_component_list(self,html):
    """Get the CBL and SGW menus"""
    component_list = html.find_all_by_class('components_list-items')
    self.component_title = component_list[0].contents[0].next.text
    return component_list

  def __build_menu_item_list(self, html):
    """This is the <div> containing all the CBL menu page links we need"""
    menu_div = html.content.find(attrs={"data-version":"3.0"})
    # So collect them together
    menu_list = menu_div.find(class_='menu_row').contents
    # Add first two generic items
    self.menu_item_list.append(menu_list[0].find('a').get('href')) # Introduction
    self.menu_item_list.append(menu_list[1].find('a').get('href')) # What's New
    """Now include the platform title [0] and each of its menu links[1]"""
    for i in range (2, 8, 1):
      platform_name = menu_list[i].contents[0].text
      href = menu_list[i].contents[0].find('a').get('href')
      print(f'Processing {platform_name} platform')
      self.menu_item_list.append(href)
      for link in menu_list[i].contents[1]:
        hrefs = link.find_all('a')
        for href in hrefs:
          self.menu_item_list.append(href.get('href'))

    return self.menu_item_list


class CouchbaseDocsPage:

  def __init__(self, url):
      self.url = url
      self.root = self.url[:self.url.rindex('/')]
      self.page = WebPage(url)
      self.html = HtmlObject(self.page.content)
      self.root = url[:url.rindex('/')]
      self.all_links = []
      self.failed_links = []
      self.get_links_from_page(True)

  def get_links(self):
    if len(self.all_links) > 0:
      return self.all_links
    else:
      return False

  def get_invalid_links(self):
    if len(self.failed_links) > 0:
      return self.failed_links
    else:
      return False

  def get_links_from_page(self, check_links):
    self.page_hrefs = []
    self.body = self.html.find_all_by_class('sect1')
    for sect in self.body:
      sect_links = sect.find_all('a')
      for link in sect_links:
        href = str(link.get('href'))
        if href != 'None':
          if (len(href) > 0 ) and not (href.startswith('#')):
            if (href.startswith('http')):
              thisHref = href
            else:
              thisHref = "{}/{}".format(self.root, href)
            self.all_links.append(thisHref)
            if check_links:
              (result, msg) = is_ValidUrl(thisHref)
              if not result:
                self.failed_links.append("{}\t{}".format(thisHref, msg))
    return True






# Test
# x = CouchbaseMenuLinks(URL)
# y = a2f(x.menu_item_list,FILENAME, PATHNAME)
# print(len(x.menu_item_list))