#!/usr/bin/python3
from tornado.web import RequestHandler
import json

class SearchHandler(RequestHandler):
    mapper = {
        'python': 'Python是目前世界最流行的AI语言',
        'java': 'Java已经是20多年的企业级应用开发语言',
        'H5': 'H5是HTML5,于2014年开始流行的前端WEB标签语言'
    }
    def get(self):
        html = """
            <h3>搜索%s结果</h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)

        # self.write(html % (wd, result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))
        self.set_status(200)  # 设置响应状态码
        # 设置响应头的数据类型
        self.set_header('Content-Type', 'application/json;charset=utf-8')

        # 设置cookie
        self.set_cookie('wd', wd)