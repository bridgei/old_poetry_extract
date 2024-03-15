from helpers import WebPage
from bs4 import BeautifulSoup as bs4


page = WebPage("https://docs.couchbase.com/home/mobile.html")



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
    # if len(search)>0:
    #   return search[0]
    # else:
    #   return False

  def find_by_class(self, search):
    return self.content.find(class_=search)
    # search = self.find_all_by_class(self, self.content.find_all(search))
    # if len(search)>0:
    #   return search[0]
    # else:
    #   return False


html = HtmlObject(page.content)
component_list = html.find_all_by_class('components_list-items')
# cl = HtmlObject(html.find_all_by_class('components_list-items'))
print(len(component_list))

# We are at component list title (e.g.Couchbase Lite/Sync Gateway)
component_title = component_list[0].contents[0].next.text

print(component_list[0].contents[0].next.text)


# This is the <div> containing all the menu page links we need
menu_div = html.content.find(attrs={"data-version":"3.0"})

menu_list = menu_div.find(class_='menu_row').contents

print(menu_list[0].find('a').get('href')) # Introduction
print(menu_list[1].find('a').get('href')) # What's New

for i in range (2, 8, 1):
  platform_name = menu_list[i].contents[0].text
  print(f'Processing {platform_name} platform')
  for link in menu_list[i].contents[1]:
    href = link.find('a').get('href')
    item = link.text
    print(f'{item} -- {href}')




# #  This prints all menu_titles
# print(html.content.find(attrs={"data-version":"3.0"}).find_all(class_='menu_title')).__getattribute__('href')

# component_into = component_list[0].contents[1]

# for component in component_list:

#   print(component)
#   # this_component = HtmlObject(component)
#   # x = HtmlObject(component.contents)
#   #  find_by_class('component_list_title').text
#   for x in component:
#     print(x)

#   # version_menu = component.find_by_class('menu_row') # get first menu row span
#   # platform_menus = version_menu.find_all_by_class('menu_row') # get the embedded menu rows (1 per platform)
#   # for platform in platform_menus:
#   #   link = HtmlObject(platform).find_all_by_tag('a')
#   #   print(link.__getattribute__('href'))

#   # version_menu = component_version.find_all_by_class()


# print(this_component.content)

# print(html.find_all_by_tag('a'))

# menu_items = []

# menu_items = html.find_by_class('menu_title')

# print(menu_items[2])


# print(HtmlObject(component))