#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 1:10 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 适配器模式
# 将一个类的接口转换成客户希望的另外一个接口。使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
# 应用场景：希望复用一些现存的类，但是接口又与复用环境要求不一致。

def printInfo(info):
    print(info)


class Player():
    '''
    适配器，将前锋中锋转为通用动作
    '''
    name = ''

    def __init__(self, name):
        self.name = name

    def Attack(self, name):
        pass

    def Defense(self):
        pass


class Forwards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("前锋%s进攻" % self.name)

    def Defense(self, name):
        printInfo("前锋%s防守" % self.name)


class Center(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("中锋%s进攻" % self.name)

    def Defense(self):
        printInfo("中锋%s防守" % self.name)


class Guards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("后卫%s进攻" % self.name)

    def Defense(self):
        printInfo("后卫%s防守" % self.name)


class ForeignCenter(Player):
    name = ''

    def __init__(self, name):
        Player.__init__(self, name)

    def ForeignAttack(self):
        printInfo("外籍中锋%s进攻" % self.name)

    def ForeignDefense(self):
        printInfo("外籍中锋%s防守" % self.name)


class Translator(Player):
    foreignCenter = None

    def __init__(self, name):
        self.foreignCenter = ForeignCenter(name)

    def Attack(self):
        self.foreignCenter.ForeignAttack()

    def Defense(self):
        self.foreignCenter.ForeignDefense()


if __name__ == '__main__':
    b = Forwards('Battier')
    m = Guards('Yao')
    ym = Translator('McGrady')

    b.Attack()
    m.Defense()
    ym.Attack()
    ym.Defense()
