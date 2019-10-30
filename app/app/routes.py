# -*- coding: utf-8 -*-
from bottle import Bottle
from apscheduler.schedulers.background import BackgroundScheduler
from .settings import *
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
