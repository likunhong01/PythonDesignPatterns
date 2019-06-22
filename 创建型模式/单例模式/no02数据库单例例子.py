# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

import sqlite3


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print(db1)
print(db2)
'''结果
<sqlite3.Cursor object at 0x1073ff0a0>
<sqlite3.Cursor object at 0x1073ff0a0>'''
