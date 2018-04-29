#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 3:35 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 职责链模式（Chain of Responsibility）：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。
# 适用场景：
# 1、有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定；
# 2、在不明确指定接收者的情况下，向多个对象中的一个提交一个请求；
# 3、处理一个请求的对象集合应被动态指定。

class BaseHandler(object):
    '''处理基类'''

    def successor(self, successor):
        # 与下一个责任者关联
        self._successor = successor


class RequestHandlerL1(BaseHandler):
    '''第一级请求处理者'''
    name = "Team Leader"

    def handle(self, request):
        if request < 500:
            print('''
Approver : Mr.%s
Amount   : US$%s
Results  : Approved''' % (self.name, format(request, ',')))
        else:
            print("\033[31;1m%s has no right to approve, handle to next.\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL2(BaseHandler):
    '''第二级请求处理者'''
    name = "Department Manager"

    def handle(self, request):
        if request < 5000:
            print('''
Approver : Mr.%s
Amount   : US$%s
Results  : Approved''' % (self.name, format(request, ',')))
        else:
            print("\033[31;1m%s has no right to approve, handle to next.\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL3(BaseHandler):
    '''第三级请求处理者'''
    name = 'Tim Cook'

    def handle(self, request):
        if request < 10000:
            print('''
Approver : Mr.%s
Amount   : US$%s
Results  : Approved''' % (self.name, format(request, ',')))
        else:
            print("\033[31;1m[%s]Too much, not approved.\033[0m" % self.name)


class RequestAPI(object):
    h1 = RequestHandlerL1()
    h2 = RequestHandlerL2()
    h3 = RequestHandlerL3()

    h1.successor(h2)
    h2.successor(h3)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def handle(self):
        '''统一请求接口'''
        self.h1.handle(self.amount)


if __name__ == '__main__':
    r1 = RequestAPI('Alex', 8688)
    r1.handle()

    for x in r1.__dict__.items():
        print('%s: %s' % (x[0], x[1]))
