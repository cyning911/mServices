#!/usr/bin/python3

from unittest import TestCase
import requests

class TestTornadoRequest(TestCase):

    base_url = 'http://127.0.0.1:9000'

    def test_index_get(self):
        url = self.base_url + '/'

        # 查询参数
        resp = requests.get(url, params={
            'wd': 'cyning',
            'title': 30
        })

        # 可能会出现400错误,原因是查询参数没有给对
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/?wd=python'

        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': 'cyning',
            'city': '杭州'
        })
        print(resp.text)

class TestCookieRequest(TestCase):
    url = 'http://127.0.0.1:9000/cookie'

    def test_search(self):
        resp = requests.get('http://127.0.0.1:9000/search', params={
            'wd': 'python'
        })
        print(resp.text)
        print(resp.cookies)
        for key in resp.cookies:
            print(key, resp.cookies.get(key))

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_delete(self):
        resp = requests.get(self.url, params={
            'name': 'token'
        })
        print(resp.text)

class TestOrderRequest(TestCase):
    url = 'http://127.0.0.1:9000/order/3/1'
    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)

class TestUserRequest(TestCase):
    url = 'http://127.0.0.1:8000/user'

    def test_login(self):
        # 上传json数据
        resp = requests.get(self.url,
                            json={
                                'name': 'cyning',
                                'pwd': '1234'
                            })
        # 读取响应的json数据
        print(resp.json())