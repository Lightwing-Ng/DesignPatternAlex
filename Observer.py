#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 3:59 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 观察者（Observer）模式又名发布-订阅（Publish/Subscribe）模式
# 当我们希望一个对象的状态发生变化，那么依赖与它的所有对象都能相应变化(获得通知),那么就可以用到Observer模式， 其中的这些依赖对象就是观察者的对象，那个要发生变化的对象就是所谓’观察者’

class ObserverBase(object):
    '''观察者基类'''

    def __init__(self):
        self._observerd_list = []

    def attach(self, observe_subject):
        '''
        添加要观察的对象
        :param observe_subject:
        :return:
        '''
        if observe_subject not in self._observerd_list:
            self._observerd_list.append(observe_subject)
            print("[%s]已经将[%s]加入观察队列..." % (self.name, observe_subject))

    def detach(self, observe_subject):
        '''
        解除观察关系
        :param observe_subject:
        :return:
        '''
        try:
            self._observerd_list.remove(observe_subject)
            print("不再观察[%s]" % observe_subject)
        except ValueError:
            pass

    def notify(self):
        '''
        通知所有被观察者
        :return:
        '''
        for objserver in self._observerd_list:
            objserver.update(self)


class Observer(ObserverBase):
    '''观察者类'''

    def __init__(self, name):
        super(Observer, self).__init__()
        self.name = name
        self._msg = ''

    @property
    def msg(self):
        '''
        当前状况
        :return:
        '''
        return self._msg

    @msg.setter
    def msg(self, content):
        self._msg = content
        self.notify()


class CCPViewer(object):
    '''
    共军被观察者
    '''

    def update(self, observer_subject):
        print('''
CCP, 收到%s消息:
%s ''' % (observer_subject.name, observer_subject.msg))


class KMTViewer(object):
    '''
    国军被观察者
    '''

    def update(self, observer_subject):
        print('''
KMT, 收到%s消息:
%s''' % (observer_subject.name, observer_subject.msg))


if __name__ == '__main__':
    obCCP = Observer("CCP Observer")
    obKMT = Observer("KMT Observer")

    ccp_1 = CCPViewer()
    kmt_1 = KMTViewer()

    obCCP.attach(ccp_1)
    obCCP.attach(kmt_1)

    obKMT.attach(kmt_1)

    obCCP.msg = "\033[32;1m敌人来了...\033[0m"

    obKMT.msg = "\033[31;1m前方发现敌人,请紧急撤离,不要告诉共军\033[0m"
