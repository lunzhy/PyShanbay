__author__ = 'Lunzhy'
from pyshanbay.shanbay import VisitShanbay
from pyshanbay import page_parser as pp

def test_bs():
    shanbay = VisitShanbay()
    shanbay.login()

    page_members = shanbay.members()
    total_page = pp.parse_pages_members(page_members)

    members_names = []
    for page in range(1, int(total_page)+1):
        page_html = shanbay.members_page(page)
        members_names += pp.parse_member_names(page_html)
    print(members_names)
    print(len(members_names))
    return
