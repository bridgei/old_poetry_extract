class CouchbaseMenuLinks:


IS_VERBOSE = False
URL = 'https://docs.couchbase.com/home/mobile.html'


  # get html content from page
  html = HtmlObject(WebPage(URL).content)

  # Get the CBL aand SGW menus
  component_list = html.find_all_by_class('components_list-items')

  # We are at component list title (e.g.Couchbase Lite/Sync Gateway)
  component_title = component_list[0].contents[0].next.text

  if IS_VERBOSE:
    print(component_list[0].contents[0].next.text)

  # This is the <div> containing all the menu page links we need
  menu_div = html.content.find(attrs={"data-version":"3.0"})

  # So collect them together
  menu_list = menu_div.find(class_='menu_row').contents

  if IS_VERBOSE:
    print(menu_list[0].find('a').get('href')) # Introduction
    print(menu_list[1].find('a').get('href')) # What's New

  for i in range (2, 8, 1):
    platform_name = menu_list[i].contents[0].text
    if IS_VERBOSE:
      print(f'Processing {platform_name} platform')
    for link in menu_list[i].contents[1]:
      href = link.find('a').get('href')
      item = link.text
    if IS_VERBOSE:
      print(f'{item} -- {href}')


