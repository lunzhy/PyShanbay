#  -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup


def test_bs():
    response = urllib.request.urlopen('http://www.shanbay.com/team/members/')
    page_html = response.read()
    soup = BeautifulSoup(page_html)
    pre = soup.prettify()
    print(pre)
    return


def login():
    cookie = http.cookiejar.CookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip,deflate',
               'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Content-Length': '99',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'pgv_pvi=7034558464; pgv_si=s7130073088; jiathis_rdc=%7B%22http%3A//www.shanbay.com/vocabtest/result/%22%3A-39112541%2C%22http%3A//www.shanbay.com/vocabtest/share/%3Fvocab%3D9000%22%3A%22163%7C1408710333623%22%7D; language_code=zh-CN; sessionid=dckzcprofzz6xvlyk4gb6woyxycvsanj; csrftoken=bW3mgY22GBOHFe8USIHrT3Zc1iZeGCkj; __utmt=1; __utma=183787513.1933368942.1408332161.1414587127.1414589766.31; __utmb=183787513.1.10.1414589766; __utmc=183787513; __utmz=183787513.1408709798.10.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
               'Host': 'www.shanbay.com',
               'Origin': 'http://www.shanbay.com',
               'Referer': 'http://www.shanbay.com/accounts/login/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}

    headers_new = {}

    post_data_origin = {'csrfmiddlewaretoken': 'bW3mgY22GBOHFe8USIHrT3Zc1iZeGCkj',
                        'username': 'ibluecoffee',
                        'password': '870625@shanbay'}

    post_data = urllib.parse.urlencode(post_data_origin)
    binary_data = post_data.encode('utf-8')
    req = urllib.request.Request(url='http://www.shanbay.com/accounts/login/', data=binary_data, headers=headers)
    opener = urllib.request.build_opener(cookie_handler)
    response = opener.open(req)
    
 
    page = response.read()
    print(page)
    soup = BeautifulSoup(page)
    pre = soup.prettify()
    print(pre)

    
    return


if __name__ == '__main__':
    login()
