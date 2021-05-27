#!/usr/bin/python3
from tornado.web import Application, RequestHandler
from app.views.cookie_v import CookieHandler
from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandler),
    ], default_host=host)
