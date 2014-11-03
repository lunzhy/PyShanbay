__author__ = 'Lunzhy'
from bs4 import BeautifulSoup
import re
import json


def _get_number_out(href):
    patt = re.compile(r'\d+')
    match = patt.search(href)
    return match.group()


def total_page_members(page_html):
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


def parse_members_info(pages):
    members = []
    for page in pages:
        soup = BeautifulSoup(page)
        soup.prettify()
        tr_members = soup.find_all('tr', {'class': 'member'})
        for tr in tr_members:
            td_infos = tr.find_all('td')

            username = td_infos[0].find_all('img')[0].get('alt')
            nickname = td_infos[0].find_all('a', {'class': 'nickname'})[0].get_text()
            userid = _get_number_out(td_infos[0].find_all('a', {'class': 'nickname'})[0].get('href'))

            points = td_infos[1].get_text()
            days = _get_number_out(td_infos[2].get_text())

            rate = td_infos[3].get_text()

            checked = True if 'label-success' in td_infos[4].find_all('span')[0].get('class') \
                else False

            member = {
                'username': username,
                'nickname': nickname,
                'userid': userid,
                'points': points,
                'days': days,
                'rate': rate,
                'checked_today': checked
            }
            members.append(member)
    return members


def parse_today_progress(progress_page):
    json_page = progress_page.decode('utf-8')  # bytes are returned
    json_data = json.loads(json_page)
    reviewed_info = json_data['data']['num_revieweds'][0]
    reviewed = reviewed_info[-1]
    if reviewed is 0:
        return False
    return True