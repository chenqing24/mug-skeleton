# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view
from ..settings import *


home_app = Bottle()

# 加载log
home_app.install(log_to_logger)


@home_app.route('/')
@jinja2_view('index.html')
def index():
    return {'get_url': home_app.get_url('/')}


@home_app.route('/health')
def health():
    '''健康检查'''
    return dict(health=True)

