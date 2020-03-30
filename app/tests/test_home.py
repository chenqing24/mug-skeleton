#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# another: Jeff.Chen
# home的接口单元测试
import unittest
from boddle import boddle 
from app.controllers.home import *


class TestHome(unittest.TestCase):
    def test_health(self):
        with boddle(path='/health'):
            print("test health()")
            # print(health())
            self.assertEqual(health(), dict(health=True))

if __name__ == '__main__':
    unittest.main()
    pass
