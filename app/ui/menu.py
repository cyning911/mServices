#!/usr/bin/python3

from tornado.web import UIModule

class MenuModule(UIModule):
    def render(self):
        data = {
            'menus': [
                {'title': '百度', 'url': 'https://www.baidu.com'},
                {'title': '淘宝', 'url': 'https://www.taobao.com'},
                {'title': '阿里', 'url': 'https://www.aliyun.com'}
            ]
        }
        # 渲染UI模块的模板
        return self.render_string('ui/menu.html', **data)