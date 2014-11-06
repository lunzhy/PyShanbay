#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import requests


class Shanbay:
    USER_AGENT = 'python-shanbay/%s' % '0.2.1'
    def __init__(self, username, password):
        self._request = requests.Session()
        self.username = username
        self.password = password

    def _attr(self, name):
        return getattr(self.__class__, name)

    def request(self, url, method='get', **kwargs):
        headers = kwargs.setdefault('headers', {})
        headers.setdefault('User-Agent', self._attr('USER_AGENT'))
        r = getattr(self._request, method)(url, **kwargs)

        return r

    def login(self, **kwargs):
        """登录"""
        url = 'http://www.shanbay.com/accounts/login/'
        r = self._request.get(url, **kwargs)
        token = r.cookies.get('csrftoken')
        data = {
            'csrfmiddlewaretoken': token,
            'username': self.username,
            'password': self.password,
            }
        return self.request(url, 'post', data=data, **kwargs).ok


if __name__ == '__main__':
    s = Shanbay('ibluecoffee', '870625@shanbay')
    a = s.login()
    print(a)