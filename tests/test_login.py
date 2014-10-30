#encoding=utf-8
__author__ = 'Lunzhy'
import requests
import copy
import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup


url_login = 'http://www.shanbay.com/accounts/login/'
headers_old = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip,deflate',
           'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Host': 'www.shanbay.com',
           'User-Agent': ' Mozilla/5.0 (Windows NT 6.2; rv:23.0) Gecko'
                         + '/20100101 Firefox/23.0'}

hostsite = urllib.parse.urlsplit('http://www.shanbay.com').netloc
print(hostsite)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Connection': 'keep-alive',
    'Host': hostsite,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                   + 'Chrome/38.0.2125.111 Safari/537.36',
}

req_first_visit = requests.get(url_login, headers=headers, stream=True)
if req_first_visit.ok:
    print('ok')
    print(req_first_visit.cookies.get_dict())

cookies_first_visit = req_first_visit.cookies.get_dict()
token = cookies_first_visit.get('csrftoken')

headers_post = copy.deepcopy(headers)
headers_post.update(
    {'Referer': url_login,
     'Content-Type': 'application/x-www-form-urlencoded',
    })
cookies_post = cookies_first_visit



print(token)
data_post_origin = {
    'csrfmiddlewaretoken': token,
    'username': 'ibluecoffee',
    'password': '870625@shanbay',
}

data_post = data_post_origin

r_login = requests.post(url_login, headers=headers_post,
                        cookies=cookies_post, data=data_post,
                        allow_redirects=False, stream=True)

print(r_login.status_code)
print(requests.codes.found)
# print r_login.url
if r_login.status_code == requests.codes.found:
    print(r_login.cookies.get_dict())



"""
cookie = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
req = urllib.request.Request(url='http://www.shanbay.com')
opener.open(req)

for c in cookie:
    if c.name == 'csrftoken':
        token = c.value

post_data_origin = {'csrfmiddlewaretoken': token,
                    'username': 'ibluecoffee',
                    'password': '870625@shanbay',
                    'login': ''}

post_data = urllib.parse.urlencode(post_data_origin).encode('utf-8')
req = urllib.request.Request(url=url_login, data=post_data)

response = opener.open(req)

for c in cookie:
    print(c.name, c.value)

page_html = response.read()
soup = BeautifulSoup(page_html)
pre = soup.prettify()
"""