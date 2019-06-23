#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class Actor(object):
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, '正在拍电影')

    def available(self):
        self.is_busy = False
        print(type(self).__name__, '正在休息')

    def get_status(self):
        return self.is_busy

class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        # 给他一个演员
        self.actor = Actor()
        # 如果在忙就休息，如果在休息就忙起来
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


# 付款的例子
class User(object):
    def __init__(self):
        self.debit_card = DebitCard()
        self.is_purchased = None

    def pay(self, card_id):
        self.is_purchased = self.debit_card.do_pay(card_id)

    def __del__(self):
        if self.is_purchased:
            print('购买成功')
        else:
            print('购买失败')


# 主题是付款，是一个抽象基类，
from abc import ABCMeta, abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# 真实主题银行类
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_acount(self):
        self.account = self.card
        return self.account

    def __has_funds(self):
        print('找到卡号：', self.__get_acount())
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print('扣款成功')
            return True
        else:
            print('扣款失败')
            return False


# 代理
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self, card_id):
        self.bank.set_card(card_id)
        return self.bank.do_pay()


user = User()
user.pay('123456')
