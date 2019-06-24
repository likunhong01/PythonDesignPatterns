# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


class Wizard(object):
    def __init__(self, src, rootdir):

        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):

        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")


if __name__ == '__main__':
    wizard = Wizard('python', 'bin')
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()

# 证券交易所的例子：
# 我想卖一个股票，在开市之前我提交给证券交易所卖股票申请，等股市一开，证券交易所就帮我卖掉

# 客户下订单的接口
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


# 具体实现类
# 买卖方法，execute来执行
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# StockTrade实现buy和sell方法
class StockTrade:
    def buy(self):
        print('买股票')

    def sell(self):
        print('卖股票')


# 调用者
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def place_order(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    # 客户端
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # 命令者
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)

    '''结果
    买股票
    卖股票'''