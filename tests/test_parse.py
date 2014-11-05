__author__ = 'Lunzhy'
from pyshanbay.shanbay import VisitShanbay
from pyshanbay import page_parser as parser
import json


def test_bs():
    shanbay = VisitShanbay()
    shanbay.login()

    page_members = shanbay.members()
    total_page = parser.total_page_members(page_members)

    members_names = []
    for page in range(1, int(total_page)+1):
        page_html = shanbay.members_page(page)
        members_names += parser.parse_member_names(page_html)

    for name in members_names:
        print(type(name))
        print(name.encode('utf-8'))
    print(len(members_names))
    return


def test_parse_info():
    shanbay = VisitShanbay()
    shanbay.login()

    page_members = shanbay.members()
    total_page = parser.total_page_members(page_members)

    pages = []

    for page in range(1, int(total_page) + 1):
        page_html = shanbay.members_page(page)
        pages.append(page_html)

    members_info = parser.parse_members_info(pages)
    for member in members_info:
        print(member)
    return


def test():
    shanbay = VisitShanbay()
    shanbay.login()

    # page = shanbay.get_progress('6684706')
    # today = parser.parse_today_progress(page)
    # print(today)

    page = shanbay.get_checkin('5537146')
    parser.paser_checkin(page)
    return