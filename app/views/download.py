#!/usr/bin/python3

from tornado.web import RequestHandler, asynchronous
from tornado.web import gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest, HTTPResponse

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

class DownloadHandler(RequestHandler):
    def get(self):
        # 获取查询参数中的url(下载资源的网站)
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename', 'index.html')

        # 发起同步请求
        client = HTTPClient()
        # validate_cert:是否验证ssl安全链接证书
        response: HTTPResponse = client.fetch(url,
                                              validate_cert=False)
        # print(response.body)
        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('下载成功')

class AsyncDownloadHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        self.write('<br>下载完成, 正在保存')
        # 在回调函数中，可以获取请求查询的参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功')
        self.finish()

    @asynchronous
    def get(self):
        # 获取查询参数中的url(下载资源的网站)
        url = self.get_query_argument('url')

        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert:是否验证ssl安全链接证书
        client.fetch(url,
                     callback=self.save,
                     validate_cert=False)

        self.write('<br>下载中……')
        self.set_status(200)

class Async2DownloadHandler(RequestHandler):
    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        self.write('<br>下载完成, 正在保存')
        # 在回调函数中，可以获取请求查询的参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功')
        self.finish()

    @asynchronous
    @gen.coroutine
    # async def get(self):
    def get(self):
        # 获取查询参数中的url(下载资源的网站)
        url = self.get_query_argument('url')

        self.write('<br>下载中……')

        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert:是否验证ssl安全链接证书
        # response = await client.fetch(url, validate_cert=False)
        response = yield client.fetch(url, validate_cert=False)
        self.save(response)

        self.set_status(200)