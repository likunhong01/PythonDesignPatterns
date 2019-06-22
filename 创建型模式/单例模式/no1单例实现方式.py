# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

'''单例模式
1.类只创建一个对象
2.为对象提供一个访问点，使程序可以全局访问该对象
3.控制共享资源的并行访问
'''


# ===============饿汉式单例===============
class Singleton1(object):
    # 通过覆盖__new__方法来控制对象的创建。
    def __new__(cls, *args, **kwargs):
        # hasattr用于查看对象cls是否有instance属性，该属性作用是检测该类是否已经生成了一个对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton1, cls).__new__(cls)
        return cls.instance


s = Singleton1()
s1 = Singleton1()
print(s)
print(s1)
'''结果：
<__main__.Singleton1 object at 0x102c3b198>
<__main__.Singleton1 object at 0x102c3b198>'''


# ===============懒汉式单例===============
class Singleton2(object):
    __instance = None

    # 初始化时，如果存在对象，就直接返回这个对象，不存在就不管，也不new它
    def __init__(self):
        if Singleton2.__instance:
            self.get_instance()

    # 实际的对象创建发生在调用get_instance的时候
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance


s = Singleton2()
print(s.get_instance())
s1 = Singleton2()
print(s1.get_instance())
'''结果：
<__main__.Singleton2 object at 0x110062240>
<__main__.Singleton2 object at 0x110062240>'''


# ===============使用元类实现单例===============
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)
'''结果：
{<class '__main__.Logger'>: <__main__.Logger object at 0x10357be10>}
{<class '__main__.Logger'>: <__main__.Logger object at 0x10357be10>}'''
