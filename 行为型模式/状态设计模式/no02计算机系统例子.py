# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


class ComputerState(object):
    name = 'state'  # 对象状态名称
    allowed = []  # 定义允许进入的状态的对象的列表

    # 改变计算机的状态的方法
    def switch(self, state):
        if state.name in self.allowed:
            print('现状态：', self, '，转换成', state.name, '成功')
            self.__class__ = state
        else:
            print('现状态：', self, '，转换成', state.name, '失败!!')

    def __str__(self):
        return self.name


# 关闭
class Off(ComputerState):
    name = 'off'
    allowed = ['on']


# 打开
class On(ComputerState):
    name = 'on'
    allowed = ['suspend', 'off', 'hibernate']


# 休眠
class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


# 挂起
class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer(object):
    # 初始状态
    def __init__(self, model='MacBook Pro'):
        self.model = model
        self.state = Off()

    # 改变状态
    def change_to(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    computer = Computer()
    computer.change_to(On)
    computer.change_to(Off)
    computer.change_to(On)
    computer.change_to(Suspend)
    # 这里不能挂起，必须要转换为on后才可以
    computer.change_to(Hibernate)
    computer.change_to(On)
    computer.change_to(Hibernate)
    computer.change_to(On)
    computer.change_to(Off)


'''结果
现状态： off ，转换成 on 成功
现状态： on ，转换成 off 成功
现状态： off ，转换成 on 成功
现状态： on ，转换成 suspend 成功
现状态： suspend ，转换成 hibernate 失败!!
现状态： suspend ，转换成 on 成功
现状态： on ，转换成 hibernate 成功
现状态： hibernate ，转换成 on 成功
现状态： on ，转换成 off 成功
'''