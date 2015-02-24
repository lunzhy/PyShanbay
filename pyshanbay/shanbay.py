__author__ = 'Lunzhy'
import urllib.parse
import urllib.request
import http.cookiejar
import copy
from urllib.parse import urlsplit
from urllib.parse import urljoin
from urllib import request
import datetime
import json
from pyshanbay.utils import ShanbayConnectException


class VisitShanbay:
    def __init__(self, username, password):
        self.base_url = 'http://www.shanbay.com'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Host': urlsplit(self.base_url).netloc,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                          'Chrome/38.0.2125.111 Safari/537.36',
        }
        self.cookie = http.cookiejar.CookieJar()
        self.cookie_processor = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(self.cookie_processor)
        self.csfrtoken = ''
        self.username = username
        self.password = password
        self.userid = ''
        return

    def home(self):
        url_login = urljoin(self.base_url, '/accounts/login/')
        req = request.Request(url=url_login)
        self.opener.open(req)
        for ck in self.cookie:
            if ck.name == 'csrftoken':
                self.csfrtoken = ck.value
        if self.csfrtoken is '':
            print('csrftoken is not obtained.')
            exit(0)
        return

    def login(self):
        self.home()
        url_login = urljoin(self.base_url, '/accounts/login/')
        headers = copy.deepcopy(self.headers)
        headers.update(
            {'Content-Type': 'application/x-www-form-urlencoded',
             'Referer': url_login,
             'Origin': self.base_url}
        )
        post_data_origin = {
            'csrfmiddlewaretoken': self.csfrtoken,
            'username': self.username,
            'password': self.password,
        }
        post_data = urllib.parse.urlencode(post_data_origin).encode('utf-8')
        req = request.Request(url=url_login, data=post_data, headers=headers)
        self.opener.open(req)
        for ck in self.cookie:
            if ck.name == 'userid':
                self.userid = ck.value
            # it is very important to refresh the csrf token, because after login a new token is set
            if ck.name == 'csrftoken':
                self.csfrtoken = ck.value

        if self.userid is '':
            raise ShanbayConnectException
            print('login error.')
        return

    def members(self):
        url_members = urljoin(self.base_url, '/team/members/')
        # it seems that headers are not required.
        req = request.Request(url=url_members, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def members_page(self, page_number):
        url_members_page = urljoin(self.base_url, '/team/members/?page=%s' % page_number)
        req = request.Request(url=url_members_page, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_progress(self, login_id):
        url_progress = urljoin(self.base_url, '/api/v1/bdc/stats/%s/?progress' % login_id)
        req = request.Request(url=url_progress, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_checkin(self, login_id):
        url_checkin = urljoin(self.base_url, '/checkin/user/%s/' % login_id)
        req = request.Request(url=url_checkin, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_server_time(self):
        # this is a temporary method
        req = request.Request(url=self.base_url, headers=self.headers)
        response = self.opener.open(req)
        time_str = response.headers.get('date')
        date_utc = datetime.datetime.strptime(time_str, '%a, %d %b %Y %H:%M:%S GMT')
        now = date_utc + datetime.timedelta(hours=8)
        return now

    def send_message(self, recipient_list, subject, message_text):
        url_sendmsg = urljoin(self.base_url, '/message/compose/')

        if isinstance(recipient_list, (list, tuple)):
            recipient = ','.join(recipient_list)
        else:
            recipient = recipient_list
        post_data_origin = {
            'csrfmiddlewaretoken': self.csfrtoken,
            'recipient': recipient,
            'subject': subject,
            'body': message_text,
        }
        post_data = urllib.parse.urlencode(post_data_origin).encode('utf-8')
        req = request.Request(url=url_sendmsg, data=post_data, headers=self.headers)
        response = self.opener.open(req)
        return response.status == 200

    def dispel_member(self, dataid_list):
        url_dismiss = urljoin(self.base_url, '/api/v1/team/member/')
        headers = copy.deepcopy(self.headers)
        headers.update(
            {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'X-Requested-With': 'XMLHttpRequest'}
        )

        if isinstance(dataid_list, (list, tuple)):
            user_ids = ','.join(map(str, dataid_list))
        else:
            user_ids = dataid_list
        post_data_origin = {
            'action': 'dispel',
            'ids': user_ids
        }
        post_data = urllib.parse.urlencode(post_data_origin).encode('utf-8')
        req = request.Request(url=url_dismiss, data=post_data, headers=headers)
        req.get_method = lambda: 'PUT'
        response = self.opener.open(req)
        content = response.read()
        ret = json.loads(content.decode('utf-8'))['status_code']
        # problem: whether the member is in the team or not, status_code 0 is returned
        return ret == 0

    def members_manage_page(self, page_number=1):
        url_page = urljoin(self.base_url, '/team/manage/?page=%s' % page_number)
        req = request.Request(url=url_page, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def visit_member_home(self, login_id):
        # http://www.shanbay.com/bdc/review/progress/1929250
        url_page = urljoin(self.base_url, '/bdc/review/progress/%s' % login_id)
        req = request.Request(url=url_page, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_member_home(self, login_id):
        return urljoin(self.base_url, '/bdc/review/progress/%s' % login_id)

    def visit_member_checkin(self, user_url):
        url_page = urljoin(self.base_url, user_url)
        req = request.Request(url=url_page, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def visit_checkin_diary_main(self, login_id):
        url_checkin = urljoin(self.base_url, '/checkin/user/%s/' % login_id)
        req = request.Request(url=url_checkin, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def visit_checkin_diary(self, login_id, page_num):
        url_checkin = urljoin(self.base_url, '/checkin/user/%s/?page=%s' % (login_id, page_num))
        req = request.Request(url=url_checkin, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

if __name__ == '__main__':
    shanbay = VisitShanbay()
    shanbay.login()
    # print(shanbay.dispel_member([590287]))


