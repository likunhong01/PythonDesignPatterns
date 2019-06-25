#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


'''
抽象对象由Trip接口表示
'''

from abc import ABCMeta, abstractmethod
# 抽象接口，定义不同日期旅行方式和地点等细节
class Trip(metaclass =ABCMeta):
    # 抽象方法，由concrete class实现，设置交通方式
    @abstractmethod
    def set_transport(self):
        pass

    # 特定日期参观地点
    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    # 创建完整行程算法
    def itinerary(self):
        self.set_transport()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


# 接下来两个具体行程继承旅行的抽象方法
class XIANTrip(Trip):
    def set_transport(self):
        print('飞机去西安')

    def day1(self):
        print('兵马俑')

    def day2(self):
        print('华清池')

    def day3(self):
        print('大明宫')

    def return_home(self):
        print('回家')


class HangZhouTrip(Trip):
    def set_transport(self):
        print('飞机去杭州')

    def day1(self):
        print('西湖')

    def day2(self):
        print('西湖')

    def day3(self):
        print('西湖')

    def return_home(self):
        print('回家')


# 旅行社根据客户选择安排旅行具体实现
class TravelAgency:
    def arrange_trip(self):
        choice = '西安'
        self.trip = XIANTrip()
        self.trip.itinerary()


TravelAgency().arrange_trip()
'''
飞机去西安
兵马俑
华清池
大明宫
回家
'''