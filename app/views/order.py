#!/usr/bin/python3

from tornado.web import RequestHandler

class OrderHandler(RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'Python高级开发',
            'author': 'cyning',
            'price': 190
        },
        {
            'id': 2,
            'name': '大数据分析',
            'author': 'cyning',
            'price': 290
        }
    ]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }

    def query(self, id):
        for item in self.goods:
            if item.get('id') == id:
                return item

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        # 在调用行为方法(get, post)之前都会调用它(RequestHandler子类对象)的initialize()方法
        print('---------initialize---------')

    def prepare(self):
        # 在初始化之后，调用行为方法之前，调用此方法进行预处理
        # 主要用于验证参数、权限、读取缓存等
        print('----------prepare----------')

    def get(self, id, code):
        print('---------get--------')
        self.write('订单查询')
        html = """
            <p>
                商品编号： %s
            </p>
            <p>
                商品名称： %s
            </p>
            <p>
                商品价格： %s
            </p>
        """
        goods = self.query(int(id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(code)))


    def post(self, code, id):
        # 所有的请求方法
        print('---------post--------')
        self.write('---------post---------')

    def on_finish(self):
        # 请求处理完成后，释放资源的方法
        # 在行为方法完成后后调用
        print('---------on_finish----------')