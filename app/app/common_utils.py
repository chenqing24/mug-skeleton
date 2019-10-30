#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# another: Jeff.Chen
# 框架级通用方法
import datetime
import logging
import logging.handlers
from functools import wraps
import socket
from bottle import request, response
 

###################
#  访问交互
###################
def enable_cors(fn):
    '''装饰器: 允许跨域访问'''
    @wraps(fn)
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)
    return _enable_cors


###################
#  log记录
###################
# Access log
logger = logging.getLogger('app')
def log_to_logger(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        request_time = datetime.datetime.now()

        # modify this to log exactly what you need:
        logger.info('%s %s %s %s %s' % (request.remote_addr,
                                        request_time,
                                        request.method,
                                        request.url,
                                        response.status))
        return fn(*args, **kwargs)
    return _log_to_logger


def get_host_ip():
    '''通过访问自己UDP方式获取准确本地IP地址'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
    

if __name__ == '__main__':
    pass
