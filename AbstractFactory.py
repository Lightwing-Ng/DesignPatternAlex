#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 11:07 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class AbstractFactory(object):
    computer_name = ''

    def createCpu(self):
        pass

    def createMainboard(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel i9-Series Computer'

    def createCpu(self):
        return IntelCpu('Intel Core i9 7980XE')

    def createMainboard(self):
        return IntelMainBoard('Intel-9000')


class AmdFactory(AbstractFactory):
    computer_name = 'Amd EPYC Computer'

    def createCpu(self):
        return AmdCpu('AMD EPYC 7601')

    def createMainboard(self):
        return AmdMainBoard('AMD-EPYC')


class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainboard(object):
    series_name = ''


class IntelMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class ComputerEngineer(object):
    def makeComputer(self, computer_obj):
        self.prepareHardwares(computer_obj)

    def prepareHardwares(self, computer_obj):
        self.cpu = computer_obj.createCpu()
        self.mainboard = computer_obj.createMainboard()

        info = '''
------- COMPUTER INFO -------
Name:\t\t%s
CPU: \t\t%s
MainBoard: \t%s
        ''' % (
            computer_obj.computer_name,
            self.cpu.series_name,
            self.mainboard.series_name
        )
        print(info)


if __name__ == '__main__':
    engineer = ComputerEngineer()  # 生成工程师实例

    computer_factory_1 = IntelFactory()  # Intel产品族
    engineer.makeComputer(computer_factory_1)

    computer_factory_2 = AmdFactory()  # AMD 产品族
    engineer.makeComputer(computer_factory_2)
