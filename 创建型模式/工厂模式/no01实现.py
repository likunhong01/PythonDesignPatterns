# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

'''简单工厂：
工厂根据传入的参数，返回或者创建不同的对象'''
# ABCMeta是Python的特殊的元类，用来生成类Abstract
from abc import ABCMeta, abstractmethod


# 动物类，定义say方法，但不实现
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


# 狗类，继承动物，重写say方法
class Dog(Animal):
    def say(self):
        print('i am dog')


# 猫类，继承动物，重写say方法
class Cat(Animal):
    def say(self):
        print('i am cat')


# 工厂类
class ForestFactory(object):
    # say方法的统一接口，传入子类对象，调用他们的say方法
    def say_something(self, object_type):
        return eval(object_type)().say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = 'Cat'
    ff.say_something(animal)
    '''结果
    i am cat'''





'''工厂方法：
1.定义一个接口来创建对象，工厂本身并不创建对象，而交给子类完成，子类决定要实例化哪些类。
2.Factory方法的创建时通过继承而不是通过实例化。
3.工厂方法更加具有可定制性，它可以返回相同的实例或者子类，而不是某种类型的对象。'''
from abc import ABCMeta, abstractmethod
# 假设每个页面都有一块区域显示个人信息，但是内容不同，设计代码如下：

# 一个区表示哪方面内容，抽象的
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# 接下来创建多个区域，用来分别显示不同的区域（简化只打印出来）
# 个人区
class PersonalSection(Section):
    def describe(self):
        print('personal section')

# 音乐部分
class AlbumSection(Section):
    def describe(self):
        print('album')

# 专利部分
class PatentSection(Section):
    def describe(self):
        print('patent')

# 出版部分
class PublicationSection(Section):
    def describe(self):
        print('publication')


# 接下来创建抽象类，提供工厂方法create_profile
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)

# 接下来创建两个具体实现工厂方法的子类
class ConcreteCreator1(Profile):
    def create_profile(self):
        # 添加个人区域、专利区域、出版区域
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())

class ConcreteCreator2(Profile):
    def create_profile(self):
        # 添加个人区域、音乐区域
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())

if __name__ == '__main__':
    # 要创建ConcreteCreator1这个对象
    profile_type = 'ConcreteCreator1'
    profile = eval(profile_type)()
    print(type(profile).__name__)
    print(profile.get_sections())
    '''结果
    ConcreteCreator1
    [<__main__.PersonalSection object at 0x10a052358>, <__main__.PatentSection object at 0x10a052390>, <__main__.PublicationSection object at 0x10a0523c8>]'''


'''抽象工厂：
1.抽象工厂主要目的是提供一个接口来创建一系列相关对象，而无需指定具体的类。
2.相比于之前的需要我们去指定创建什么对象，抽象工厂不需要。'''
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    # 有蔬菜的披萨
    @abstractmethod
    def create_veg_pizza(self):
        pass

    # 没蔬菜的披萨
    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class USAPizzaFactory(PizzaFactory):
    # USA披萨店里有蔬菜的披萨是玉米披萨
    def create_veg_pizza(self):
        return CornPizza()

    # USA店里没蔬菜的披萨是牛肉披萨
    def create_non_veg_pizza(self):
        return BeefPizza()


class ChinaPizzaFactory(PizzaFactory):
    # 中国披萨店里有蔬菜的披萨是水果披萨
    def create_veg_pizza(self):
        return FruitsPizza()

    # 中国披萨店里没有蔬菜的披萨是羊肉披萨
    def create_non_veg_pizza(self):
        return MuttonPizza()


# 接下来定义4种披萨和他们的父类（有蔬菜和无蔬菜）
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, veg_pizza):
        pass


# 没蔬菜的披萨在有蔬菜的披萨上面加肉就可以
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class CornPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class BeefPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，牛肉是加在', type(veg_pizza).__name__,'里面的')


class FruitsPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class MuttonPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，羊肉是加在', type(veg_pizza).__name__,'里面的')


class PizzaStore(object):
    def __init__(self):
        pass

    def make_pizzas(self):
        # 创建的是所有对象（所有披萨），而不是单个指定对象
        for factory in [USAPizzaFactory(), ChinaPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            # 调用
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


pizza = PizzaStore()
pizza.make_pizzas()
