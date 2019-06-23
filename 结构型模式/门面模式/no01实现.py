# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


# 酒店类，预定酒店
class Hotelier(object):
    def __init__(self):
        pass

    def __is_available(self):
        return True

    def book_hotel(self):
        if self.__is_available():
            print('预定了酒店')


# 花卉类
class Florist(object):
    def __init__(self):
        print('初始化放花的类')

    def set_flowers(self):
        print('放了好多花')


# 宴席类
class Caterer(object):
    def __init__(self):
        pass

    def set_cuisine(self):
        print('有好多吃的')


# 音乐类
class Musician(object):
    def __init__(self):
        pass

    def set_music(self):
        print('放音乐')


# 经理类
class EventManager(object):
    def __init__(self):
        pass

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()  # 订酒店

        self.florist = Florist()
        self.florist.set_flowers()  # 放花

        self.caterer = Caterer()
        self.caterer.set_cuisine()  # 定菜

        self.musician = Musician()
        self.musician.set_music()  # 放音乐


class You(object):
    def __init__(self):
        print('我的任务开始')

    def let_manager_work(self):
        EventManager().arrange()

    def __del__(self):
        print('我的任务结束')


you = You()
you.let_manager_work()
'''结果：
我的任务开始
预定了酒店
初始化放花的类
放了好多花
有好多吃的
放音乐
我的任务结束'''