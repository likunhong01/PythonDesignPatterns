# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


# 模型-视图-控制器模式
class Model:
    services = {
        'email':
            {
                'number': 1000,
                'price': 2,
            },
        'sms':
            {
                'number': 1000,
                'price': 10,
            },
        'voice':
            {
                'number': 1000,
                'price': 15,
            }
    }


class View:
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print(Model.services[svc]['number'],
                  '条',
                  svc,
                  '消息你应该支付',
                  Model.services[svc]['price'],
                  '元')


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


def Client():
    controller = Controller()
    print('我们提供:')
    controller.get_services()
    print('他们的价格是：')
    controller.get_pricing()


Client()
