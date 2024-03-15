from bs4 import BeautifulSoup
from requests_html import HTMLSession
from TextFileClasses import ArrayToFile as af

from config import URL
# import data
from validURL import is_ValidUrl

IS_VERBOSE = False
BASEURL = 'https://suchness1.wordpress.com/'
URL = f'{BASEURL}2023/10/29/toadstools-on-a-beech-stump/'
CAT_POETRY_URL = f'{BASEURL}category/poetry/'
FILENAME = 'suchness_sample.txt'
DATALIB='../data/suchness/'


def collate_poem(par_session, par_url):
    '''Returns the poem title and body as a tuple'''
    session = par_session
    r = session.get(par_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for br in soup.select("br"):
        br.replace_with("\n")

    verses = soup.find_all('pre')
    this_verse = verses[0].getText()
 #   for br in soup.select("br"):
  #      br.replace_with("\n")
#    print(f'{this_verse}')
    poem = [soup.find_all('title')[0].getText()]
    poem.append(this_verse)
    return poem


def collate_poem_list(par_session, par_url):
    this_list = []
    session = par_session
    r = session.get(par_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    poem_titles = soup.find_all('h2', {"class": "wp-block-post-title"})
    for t in poem_titles:
        this_list.append(t.find("a").get('href'))
#    print(f'ended with {len(this_list)} items')
    return(this_list)


def main (url):
    """Main Web Object Project Function"""

    this_session = HTMLSession()

    poem_links = collate_poem_list(par_session = this_session, par_url=CAT_POETRY_URL)
    for poem in poem_links:
        this_page = collate_poem(par_session=this_session, par_url=poem)
        print(f'Title = {this_page[0]}')
        print(f'Body = {this_page[1]}')

        with open(f'{DATALIB}poems/{this_page[0]}','w') as of:
            of.write(f'{this_page[0]}\n\n')
            of.write(f'{this_page[1]}')
        of.close()
    print('stopped')




if __name__ ==  "__main__":
  main(URL)
