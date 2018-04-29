#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 4:27 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import time


class foo(object):
    def f1(self):
        print("Original f1")

    def f2(self):
        print("Original f2")


class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print(
            'decorated f1 @ %s.' % time.strftime(
                '%Y/%m/%d %H:%M:%S', time.localtime()
            )
        )
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


u = foo()
v = foo_decorator(u)  # v为修饰u后的结果

v.f1()
v.f2()
