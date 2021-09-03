#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import click
from bottle import static_file, Bottle, run, TEMPLATE_PATH
from beaker.middleware import SessionMiddleware


@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--ip', default='0.0.0.0', type=str,
              help=u'Set application server ip!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
@click.option('--dev', default=False,
              help=u'Set run env is dev!') 
def runserver(port, ip, debug, dev=False):
    click.echo('Start server at: {}:{}'.format(ip, port))

    if dev and 'true' == str(dev).lower():
        # 设置运行环境
        os.environ['run_env']='dev'

    if 'true' == str(debug).lower():
        debug = True

    # 加载bottle

    from app import settings
    from app.routes import Routes


    TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)
    session_opts = {
        'session.type': 'file',
        'session.auto': True
    }

    app = SessionMiddleware(Bottle(), session_opts)

    # Bottle Routes
    app.wrap_app.merge(Routes)

    @app.wrap_app.route('/assets/<path:path>', name='assets')
    def assets(path):
        yield static_file(path, root=settings.STATIC_PATH)

    run(app=app, host=ip, port=port, debug=debug, reloader=debug)
    # TODO 使用gunicorn启动多进程，不再支持port和自定义传参，不能调试；如果debug，用原方法启动
    # run(server='gunicorn', workers=4, app=app, host='0.0.0.0', port=9999, debug=debug, reloader=debug)


@cmds.command()
def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


if __name__ == "__main__":
    cmds()
