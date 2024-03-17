from bs4 import BeautifulSoup
from requests_html import HTMLSession
from TextFileClasses import ArrayToFile as af
from dataclasses import dataclass
from config import URL
# import data
from validURL import is_ValidUrl
from pathvalidate import FilePathSanitizer, sanitize_filename
import string
import re

IS_VERBOSE = False
BASEURL = 'https://suchness1.wordpress.com/'
URL = f'{BASEURL}2023/10/29/toadstools-on-a-beech-stump/'
CAT_POETRY_URL = f'{BASEURL}category/poetry/'
FILENAME = 'suchness_sample.txt'
DATALIB='../data/suchness/'
ALPHANUMERIC = r'[^A-Za-z0-9_]+'
@dataclass
class Poem_Data:
    poem_title: str
    poem_verses: str = ''
    poem_context: str = ''
    poem_url: str = ''
    poem_file: str = ''



def get_poem_context(par_verses: list):
    this_verses = par_verses[0].fetchPreviousSiblings()
    this_context=''
    for this_item in this_verses:
        this_context= f'{this_context}{this_item.getText()}'
    return this_context

def collate_poem(par_session, par_url):
    '''Returns the poem_page title and body as a tuple'''
    this_poem = ''
    poem_data = Poem_Data
    this_title = ''
    this_context = ''
    this_session = par_session
    # get web page
    this_page = this_session.get(par_url)
    soup = BeautifulSoup(this_page.content, 'html.parser')
    for br in soup.select("br"):
        br.replace_with("\n")

    # get all poem_page verses from page
    these_verses = soup.find_all('pre')

    # Collate text from all verse elements
    if len(these_verses)>0:
        for v in these_verses:
            this_poem = f'{this_poem}{v.getText()}'

    # Get any none verse content such as poem_page context and-or preambles
    this_context = get_poem_context(these_verses)

    #x=verses[0].fetchPreviousSiblings()
    #z=''
    #q=x
    #for y in x:
    #    z= f'{z}{y.getText()}'
    #if len(z)>0:
    #    print(f'{z}')

    #else:
    #    this_poem = f''
        #print('empty file found')

    # Get poem title text
    this_title = soup.find_all('title')[0].getText().strip()
    this_title = str(this_title.replace(' – Suchness1',''))
    for c in this_title:
        if c == '\u2026':
            print(f'character is ££{c}££')
    # poem_page[0] = str(poem_page[0]).replace(' – Suchness1','')

    poem_page = []
    poem_page.append(this_title)
    poem_page.append(this_context)
    poem_page.append(this_poem)

    poem_data.poem_verses = this_poem
    poem_data.poem_context = this_context
    poem_data.poem_title = this_title.strip()
#    if '\u2026' in this_title:
#        temp = this_title.replace('\u2026','').strip()
#    else:
#        temp = this_title.strip()
        #print(f'character is ££{c}££')
#    poem_data.poem_file = this_title.translate(str.maketrans('', '', string.punctuation))
    poem_data.poem_file = (this_title.replace('\u2026','').strip().replace(' ','_')).strip()
    #poem_data.poem_file = (poem_data.poem_file.replace('\u2026','')).strip()
    poem_data.poem_file =    re.sub(ALPHANUMERIC, '', poem_data.poem_file).strip()
 #   poem_data.poem_file = poem_data.poem_file.replace(' ', '_')
  # poem_data.poem_file = poem_data.poem_file.replace('...', '')

    poem_data.poem_url = par_url
    if '\u2026' in this_title:
        print('check')
    return poem_data
    #return poem_page


def collate_poem_list(par_session, par_url):
    this_list = []
    session = par_session
    r = session.get(par_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    poem_list_pages = soup.find_all( 'div', {"class": 'wp-block-query-pagination-numbers'})
    x=poem_list_pages[0].text.split('\n')
    print(len(x))
    num_poem_pages = int(x[len(x)-1])

    print(f'Poem pages = {num_poem_pages}')
    for i in range(num_poem_pages):
        if i>0:
            # get next url
            r = session.get(f'{par_url}page/{str(i + 1)}')
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


    for this_link in poem_links:
        #my_poem_data = Poem_Data
        poem_data = collate_poem(par_session=this_session, par_url=this_link)
        if len(f'{poem_data.poem_verses}')>0:
            print(f'Processing = {poem_data.poem_title}')
            #print(f'Body = {this_page[1]}')
            with open(f'{DATALIB}poems/{poem_data.poem_file}.txt','w') as of:
                of.write(f'{poem_data.poem_title}\n\n')
                of.write(f'{poem_data.poem_context}\n\n')
                of.write(f'{poem_data.poem_verses}\n\n')
                of.write(f'\n\n{poem_data.poem_url}')

            of.close()
        else:
            print(f'Empty File = {poem_data.poem_title} page = {this_link}')
    print('stopped')


def savestuff(this_page: list):
    if len(f'{this_page[1]}') > 0:
        print(f'Processing = {this_page[0]}')
        # print(f'Body = {this_page[1]}')
        with open(f'{DATALIB}poems/{this_page[0]}', 'w') as of:
            for i in range(3):
                of.write(f'{this_page[i]}\n\n')
        #                of.write(f'{this_page[1]}\n\n')
        of.close()
    else:
        print(f'Empty File = {this_page[0]} page = {this_link}')



if __name__ ==  "__main__":
  main(URL)
