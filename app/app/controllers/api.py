#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# another: Jeff.Chen
# "/api"映射的访问接口 
from bottle import Bottle, jinja2_view
from ..settings import *


###################
# 初始化app，加载中间件
###################
api_app = Bottle()

# 加载log
api_app.install(log_to_logger)


@api_app.get('/')
@jinja2_view('index.html')
@enable_cors
def index():
    return {'get_url': api_app.get_url('/')}



if __name__ == '__main__':
    pass
