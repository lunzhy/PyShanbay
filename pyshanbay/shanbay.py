__author__ = 'Lunzhy'
import urllib.parse
import urllib.request
import http.cookiejar
import copy
from urllib.parse import urlsplit
from urllib.parse import urljoin
from urllib import request


class VisitShanbay:
    def __init__(self):
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
        self.username = 'ibluecoffee'
        self.password = '870625@shanbay'
        self.userid = ''
        return

    def home(self):
        home_url = self.base_url
        req = request.Request(url=home_url)
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
        if self.userid is '':
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

    def get_progress(self, userid):
        url_progress = urljoin(self.base_url, '/api/v1/bdc/stats/%s/?progress' % userid)
        req = request.Request(url=url_progress, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_checkin(self, userid):
        url_checkin = urljoin(self.base_url, 'http://www.shanbay.com/checkin/user/%s/' % userid)
        req = request.Request(url=url_checkin, headers=self.headers)
        response = self.opener.open(req)
        page_html = response.read()
        return page_html

    def get_server_time(self):
        # this is a temporary method
        import datetime
        now = datetime.datetime.now()
        print(now)
        return now


if __name__ == '__main__':
    shanbay = VisitShanbay()
    shanbay.login()
    shanbay.members()