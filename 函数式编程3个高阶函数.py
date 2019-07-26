# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

# map用法
list(map(lambda x: x * 2, range(10)))
# 和列表生成式结果一样，还是推荐用列表生成式
[i * 2 for i in range(10)]

# reduce归约用法
from functools import reduce

reduce(lambda x, y: x + y, range(1, 6))
# 相当于从1开始，1，2作为xy，加起来，然后再把结果作为x，后一个作为y再演算
# ((((1+2)+3)+4)+5)


# filter用法
filter(lambda x: x % 2 == 0, range(10))
[i for i in range(10) if i % 2 == 0]
