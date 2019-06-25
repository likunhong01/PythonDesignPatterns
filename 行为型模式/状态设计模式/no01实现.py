# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handel(self):
        pass


class ConcreteStateA(State):
    def handel(self):
        print('A')


class ConcreteStateB(State):
    def handel(self):
        print('B')


class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handel(self):
        self.state.handel()


context = Context()
sA = ConcreteStateA()
sB = ConcreteStateB()
context.set_state(sA)
context.handel()
