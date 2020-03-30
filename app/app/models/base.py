#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# another: Jeff.Chen
# ORM基类 
from peewee import *
from playhouse.pool import PooledMySQLDatabase
from playhouse.db_url import connect
from ..settings import *


# Connect to a MySQL database
# db = PooledMySQLDatabase(
#     DB_CONNECT_DB, 
#     user=DB_CONNECT_USER, 
#     password=DB_CONNECT_PASSWORD,
#     host=DB_CONNECT_HOST, 
#     port=DB_CONNECT_PORT,
#     max_connections=20,
#     autoconnect=True)
# db.connect()
# db = connect(DB_CONNECT_URL)
db = SqliteDatabase(DB_CONNECT_URL)


class BaseModel(Model):
    '''基类绑定db'''
    class Meta:
        if db.is_closed():
            db.connect()
        database = db
    

if __name__ == '__main__':
    pass