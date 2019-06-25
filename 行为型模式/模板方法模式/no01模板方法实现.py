# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

from abc import ABCMeta, abstractmethod


# 通用编译器接口
class Compiler(object):
    @abstractmethod
    def collect_Source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_Source()
        self.compile_to_object()
        self.run()


# ios编译器具体实现
class IOSCompiler(Compiler):
    def compile_to_object(self):
        print('把swift转化成LIVM二进制代码')

    def run(self):
        print('运行起来了')

    def collect_Source(self):
        print('收集swift代码源码')


if __name__ == '__main__':
    ios = IOSCompiler()
    ios.compile_and_run()


