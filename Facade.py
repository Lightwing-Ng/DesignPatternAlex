#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 2:37 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 外观模式（Facade），为子系统中的一组接口提供一个一致的界面，定义一个高层接口，这个接口使得这一子系统更加容易使用。
# 在以下情况下可以考虑使用外观模式：
# (1)设计初期阶段，应该有意识的将不同层分离，层与层之间建立外观模式。
# (2) 开发阶段，子系统越来越复杂，增加外观模式提供一个简单的调用接口。
# (3) 维护一个大型遗留系统的时候，可能这个系统已经非常难以维护和扩展，但又包含非常重要的功能，为其开发一个外观类，以便新系统与其交互。

# 优点编辑
# （1）实现了子系统与客户端之间的松耦合关系。
# （2）客户端屏蔽了子系统组件，减少了客户端所需处理的对象数目，并使得子系统使用起来更加容易。


def printInfo(info):
    print(info)


class Stock():
    name = 'BABA'

    def buy(self):
        printInfo('Buy ' + self.name)

    def sell(self):
        printInfo('Sale ' + self.name)


class ETF():
    name = 'IndexFund'

    def buy(self):
        printInfo('Buy ' + self.name)

    def sell(self):
        printInfo('Sale ' + self.name)


class Future():
    name = 'FUTU'

    def buy(self):
        printInfo('Buy ' + self.name)

    def sell(self):
        printInfo('Sale ' + self.name)


class NationDebt():
    name = 'US'

    def buy(self):
        printInfo('Buy ' + self.name)

    def sell(self):
        printInfo('Sale ' + self.name)


class Option():
    name = 'Warrants'

    def buy(self):
        printInfo('Buy ' + self.name)

    def sell(self):
        printInfo('Sale ' + self.name)


class Fund():
    def __init__(self):
        self.stock = Stock()
        self.etf = ETF()
        self.future = Future()
        self.debt = NationDebt()
        self.option = Option()

    def buyFund(self):
        self.stock.buy()
        self.etf.buy()
        self.debt.buy()
        self.future.buy()
        self.option.buy()

    def sellFund(self):
        self.stock.sell()
        self.etf.sell()
        self.future.sell()
        self.debt.sell()
        self.option.sell()


if __name__ == '__main__':
    myFund = Fund()
    myFund.buyFund()
    myFund.sellFund()
