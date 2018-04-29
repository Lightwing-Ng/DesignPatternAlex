#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 4:18 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class TravelStrategy(object):
    '''
    出行策略基类
    '''

    def travelAlgorithm(self):
        pass


class AirplaneStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print('Travel by air...')


class TrainStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print('Travel by High Speed Railway...')


class CarStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print('Travel by self-driving...')


class BicycleStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("Travel by bicycle...")


class TravelInterface(object):
    def __init__(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def set_strategy(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def travel(self):
        return self.travel_strategy.travelAlgorithm()


if __name__ == '__main__':
    # 坐飞机
    travel = TravelInterface(AirplaneStrategy())
    travel.travel()

    # 改开车
    travel.set_strategy(TrainStrategy())
    travel.travel()
