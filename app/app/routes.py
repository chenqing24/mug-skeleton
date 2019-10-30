# -*- coding: utf-8 -*-
from bottle import Bottle
from apscheduler.schedulers.background import BackgroundScheduler
from .settings import *
from .models.base import db
from .controllers.home import home_app
from .controllers.api import api_app


###################
#  访问路由定义
###################
Routes = Bottle()
# App to render / (home)
Routes.merge(home_app)

# 加载用户自定义bottle app
Routes.mount('/api', api_app)

# db与框架访问整合
@api_app.hook('before_request')
def _connect_db():
    if db.is_closed():
        db.connect()

@api_app.hook('after_request')
def _close_db():
    if not db.is_closed():
        db.close()


###################
#  db相关
###################
def create_tables():
    '''模型建表'''
    # TODO 用户自定义表模型在这里添加
    table_model_list = []
    if table_model_list:
        with db:
            db.create_tables(table_model_list)

# DB建表
create_tables()


###################
#  后台调度任务
###################
scheduler = BackgroundScheduler()
if scheduler.get_jobs():
    # 清空原有任务，防止执行异常
    scheduler.remove_all_jobs()

# TODO demo任务
def demo_task():
    print("current env: {}".format(CURRENT_RUNTIME_ENV))

scheduler.add_job(
    demo_task,
    trigger="interval",
    seconds=60
)


# TODO 调试不开启调度
if scheduler.state != 1:
    scheduler.start()
