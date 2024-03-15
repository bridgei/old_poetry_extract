# from helpers import WebElement
from selenium import webdriver
# from helpers import WebPage
# from helpers import Browser
from CouchbaseMenuLinksClasses import CouchbaseMenuLinks
from CouchbaseMenuLinksClasses import CouchbaseDocsPage
from HtmlObjectClasses import HtmlObject
from WebObjectClasses import WebPage
from TextFileClasses import ArrayToFile  as A2F
from config import URL
# import data
from validURL import is_ValidUrl

IS_VERBOSE = False
BASEURL = 'https://docs.couchbase.com'
URL = 'https://docs.couchbase.com/home/mobile.html'
FILENAME = 'cbl-menu-link.txt'
PATHNAME = 'data'


def main (url):
  """Main Web Object Project Function"""

  couchbaseMenuItems = CouchbaseMenuLinks(URL).menu_item_list
  # y = A2F(couchbaseMenuItems.menu_item_list,FILENAME, PATHNAME)
  # print(len(couchbaseMenuItems.menu_item_list))

  # trial_list = couchbaseMenuItems.menu_item_list
    # [
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/android/p2psync-websocket-using-active.html#api-references',
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/c/p2psync-websocket-using-active.html#api-references',
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/csharp/p2psync-websocket-using-active.html#api-references',
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/java/p2psync-websocket-using-active.html#api-references',
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/objc/p2psync-websocket-using-active.html#api-references',
    # 'https://docs-staging.couchbase.com/couchbase-lite/current/swift/p2psync-websocket-using-active.html#api-references'
    # 'https://docs.couchbase.com/couchbase-lite/3.0/c/gs-downloads.html',
    # 'https://docs.couchbase.com/couchbase-lite/3.0/android/gs-install.html',
    # 'https://docs.couchbase.com/couchbase-lite/3.0/android/database.html'
  # ]

  failed_links = {}
  platform = 'platform'
  pagename = 'pagename'

  for menuItem in couchbaseMenuItems:
    # For each menu item create a list of HREFs from its page content

    if (str(menuItem).find('couchbase-lite')):
      if str(menuItem).startswith('../couchbase-lite/3.0/'):
        thisURL = str(menuItem).replace('../couchbase-lite/3.0/',
                                        'https://docs-staging.couchbase.com/couchbase-lite/current/')
      else:
        thisURL = str(menuItem)
      if (str(thisURL).count('/') > 5):
        platform = thisURL.split('/')[5]
        pagename = thisURL.split('/')[6].split('.')[0]
        print(f'Collating {platform}/{pagename}\n')
        thisFiledLinksList = CouchbaseDocsPage(thisURL)
        failed_links[f'{platform}/{pagename}'] = thisFiledLinksList.failed_links
    print(f'Processed and collected {len(failed_links)}')
    filename = "{}-{}".format(platform, pagename)
    if A2F(failed_links, filename, PATHNAME):
      print(f'Saved {filename}')
  print('exit')

  # Crawl site to validate each collected link
  # for key, value in links_to_check.items():
  #   filename = str(key).replace('/','_')
  #   failed_links = []
  #   print(f'Validating {key}\n')
  #   for item in value:
  #     if item != "None":
  #       thisItem = str(item)
  #       if thisItem.startswith('http'):
  #         (result, msg) =  is_ValidUrl(thisItem)
  #         if not result:
  #           failed_links.append(f'Invalid url = {thisItem} msg = {msg}')
  #   save = A2F(failed_links, filename, PATHNAME)
  #   print(f'Key: {key} = {save.count}\n')




if __name__ ==  "__main__":
  main(URL)
