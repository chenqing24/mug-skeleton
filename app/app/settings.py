# -*- coding: utf-8 -*-
import os
from .common_utils import *


###################
#  环境变量
###################

# 设定response反馈json
response.content_type = 'application/json'

# 本地IP
LOCAL_IP = get_host_ip()

# 项目相关路径
PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')

# 运行环境，根据实际情况修改
ENV_PROD = 'prod'
ENV_INTE = 'inte'
# 所有环境集合，用于check
ALL_ENV_SETS = (ENV_PROD, ENV_INTE)
# 当前运行环境，根据网段修改
CURRENT_RUNTIME_ENV = ENV_PROD
if str(LOCAL_IP).startswith('172.'):
    CURRENT_RUNTIME_ENV = ENV_PROD
elif str(LOCAL_IP).startswith('10.'):
    CURRENT_RUNTIME_ENV = ENV_INTE
else:
    raise RuntimeError('未知运行环境，请联系管理员')


###################
#  log配置
###################
# Access log等级
logger.setLevel(logging.INFO)
# Access log存放路径
LOG_PATH = PROJECT_PATH + '/../log/'
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
# Access log文件名
LOG_FILE = LOG_PATH + 'app.log'
# log保留策略 50M*10
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, 
    maxBytes=50*1024*1024, 
    backupCount=10)
formatter = logging.Formatter('%(msg)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# peewee orm logging
logger_orm = logging.getLogger('peewee')
logger_orm.addHandler(logging.StreamHandler())
logger_orm.setLevel(logging.INFO)


###################
#  db相关
###################
# 数据库连接
DB_CONNECT_DB       = 'demo'
DB_CONNECT_USER     = 'root'
DB_CONNECT_PASSWORD = 'my-secret-pw'
DB_CONNECT_HOST     = '127.0.0.1'
DB_CONNECT_PORT     = 3306


###################
#  用户自定义常量
###################
