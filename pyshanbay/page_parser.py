__author__ = 'Lunzhy'
from bs4 import BeautifulSoup
import re
import json
import datetime

_Chinese_number = {'一': '1', '二': '2', '三': '3', '四': '4', '五': '5', '六': '6',
                   '七': '7', '八': '8', '九': '9', '十': '10', '十一': '11', '十二': '12'}


def _get_number_out(href):
    patt = re.compile(r'\d+')
    match = patt.search(href)
    return match.group()


def _regex_search(patt, search_str):
    re_patt = re.compile(patt)
    match = re_patt.search(search_str)
    if match is not None:
        return match.group()
    else:
        return ''


def _parse_chinese_date(date_str):
    chinese_month = _regex_search(r'.+(?=月)', date_str)
    month = _Chinese_number[chinese_month]
    day = _regex_search('\d+(?=,)', date_str)
    year = _regex_search('(?<=, )\d+', date_str)
    dt = datetime.date(int(year), int(month), int(day))
    return dt


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
            login_id = _get_number_out(td_infos[0].find_all('a', {'class': 'nickname'})[0].get(
                'href'))

            points = td_infos[1].get_text()
            days = _get_number_out(td_infos[2].get_text())

            rate = td_infos[3].get_text()

            checked = True if 'label-success' in td_infos[4].find_all('span')[0].get('class') \
                else False

            member = {
                'username': username,
                'nickname': nickname,
                'login_id': login_id,
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


def parse_recent_progress(progress_page):
    json_page = progress_page.decode('utf-8')
    json_data = json.loads(json_page)
    nums_recent = json_data['data']['num_today']
    reviewed_recent = json_data['data']['num_revieweds']
    return nums_recent, reviewed_recent


def paser_checkin(checkin_page):
    soup = BeautifulSoup(checkin_page)
    soup.prettify()
    div_checkins = soup.find_all('div', {'class': 'checkin span8'})
    notes, dates = [], []
    for checkin in div_checkins:
        note = checkin.find_all('div', {'class': 'note'})[0].get_text().strip()
        date = checkin.find_all('div', {'class': 'span4'})[0].get_text().strip()
        notes.append(note)
        dates.append(date)

    notes, dates = notes[:7], dates[:7]  # only get 7 items
    words = [_regex_search(r'\d+(?= 个单词)', note) for note in notes]
    reads = [_regex_search(r'\d+(?= 篇文章)', note) for note in notes]
    sents = [_regex_search(r'\d+(?= 个句子)', note) for note in notes]

    dates = [_parse_chinese_date(date) for date in dates]
    checkin_list = []

    for date, word, read, sent in zip(dates, words, reads, sents):
        word = 0 if word == '' else int(word)
        read = 0 if read == '' else int(read)
        sent = 0 if sent == '' else int(sent)
        checkin = {'words': word, 'reads': read, 'sents': sent}
        date_checkin = [date, checkin]
        checkin_list.append(date_checkin)

    return checkin_list


def parse_members_manage(pages, shanbay):
    members = []
    for page in pages:
        soup = BeautifulSoup(page)
        soup.prettify()
        tr_members = soup.find_all('tr', {'class': 'member'})
        for tr in tr_members:
            # a new data-id is assigned to member when he joins the team
            data_id = tr.get('data-id')
            nickname = tr.get('data-name')

            td_infos = tr.find_all('td')

            user_url = td_infos[0].find_all('a', {'class': 'nickname'})[0].get('href')
            username = parse_username(shanbay.visit_member_checkin(user_url))

            login_id = _get_number_out(td_infos[0].find_all('a', {'class': 'nickname'})[0].get(
                'href')).strip()

            points = td_infos[1].get_text().strip()
            days = _get_number_out(td_infos[2].get_text()).strip()
            rate = td_infos[3].get_text().strip()
            checkin_yesterday = True if 'label-success' in td_infos[4].find_all('span')[0].get(
                'class') else False
            checkin_today = True if 'label-success' in td_infos[5].find_all('span')[0].get(
                'class') else False

            member = {
                'login_id': login_id,
                'username': username,
                'nickname': nickname,
                'data_id': data_id,
                'points': points,
                'days': days,
                'rate': rate,
                'checkin_today': checkin_today,
                'checkin_yesterday': checkin_yesterday
            }
            members.append(member)
    return members


def parse_total_checkin(page):
    soup = BeautifulSoup(page)
    soup.prettify()
    ul = soup.find_all('ul', {'class': 'nav-stacked'})
    checkins = ul[0].find_all('a')[1].get_text()
    days = _get_number_out(checkins)
    return days


def parse_username(page):
    soup = BeautifulSoup(page)
    soup.prettify()
    t = soup.find_all(class_='page-header')[0].find_all('h2')[0].text.strip()
    return t.strip(r'的日记').strip()