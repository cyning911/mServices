#!/usr/bin/python3
import os

from tornado.web import Application, RequestHandler

from app.ui.menu import MenuModule
from app.ui.nav import NavModule
from app.views.cookie import CookieHandler
from app.views.index import IndexHandler
from app.views.order import OrderHandler
from app.views.search import SearchHandler
from app.views.download import DownloadHandler, AsyncDownloadHandler, Async2DownloadHandler
from app.views.message import RobotHandler, MessageHandler
from app.views.user import UserHandler


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules': {
        'Nav': NavModule,
        'Menu': MenuModule
    },
    'cookie_secret': 'fsdfr34530f*&*Hob'
}

def make_app(host='localhost'):

    return Application(handlers=[
                      ('/', IndexHandler),
                      ('/search', SearchHandler),
                      ('/cookie', CookieHandler),
                      ('/download', DownloadHandler),
                      ('/download2', AsyncDownloadHandler),
                      ('/download3', Async2DownloadHandler),
                      ('/robot', RobotHandler),
                      ('/message', MessageHandler),
                      ('/login', UserHandler),
                      (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandler),
    ], default_host=host, **settings)
