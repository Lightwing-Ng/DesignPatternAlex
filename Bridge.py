#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 1:37 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class AbstractRoad(object):
    '''公路基类'''
    car = None


class AbstractCar(object):
    '''车辆基类'''

    def run(self):
        pass


class People(object):
    '''Human kind'''
    pass


class Street(AbstractRoad):
    '''市区街道'''

    def run(self):
        self.car.run()
        print("华强北的街道上行驶")


class SpeedWay(AbstractRoad):
    '''高速公路'''

    def run(self):
        self.car.run()
        print("高速公路上行驶")


class Car(AbstractCar):
    '''小汽车'''

    def run(self):
        print("小汽车在", end='')


class Phaeton(AbstractCar):
    '''顶配辉腾'''

    def run(self):
        print("顶配辉腾在", end='')


class Woman(People):
    def drive(self):
        print("钟晓迪开着", end='')
        self.road.run()


class Man(People):
    def drive(self):
        print("唐宇恒开着", end='')
        self.road.run()


if __name__ == '__main__':
    # 钟晓迪开着顶配辉腾在市区街道上行驶
    road_1 = Street()
    road_1.car = Phaeton()
    p1 = Woman()
    p1.road = road_1
    p1.drive()

    # 唐宇恒开着顶配辉腾在高速公路上行驶
    road_2 = SpeedWay()
    road_2.car = Phaeton()
    p2 = Man()
    p2.road = road_2
    p2.drive()
