__author__ = 'Lunzhy'
from bs4 import BeautifulSoup


def parse_pages_members(page_html):
    soup = BeautifulSoup(page_html)
    soup.prettify()
    links_page = soup.find_all('a', {'class': 'endless_page_link'})
    page_last = links_page[-2].text  # the second last number is total page number
    return page_last


def parse_member_names(page_num):
    soup = BeautifulSoup(page_num)
    soup.prettify()
    table_trs = soup.find_all('tr', {'class': 'member'})
    nicknames = []
    for tr in table_trs:
        td = tr.find('td', {'class': 'user'})
        name = td.find('a', {'class': 'nickname'})
        nicknames.append(name.text)
    return nicknames


