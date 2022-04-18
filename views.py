import datetime

from flower_shelf_framework.templator import render
from patterns.creational_patterns import Engine, decode_data, Parameter
from patterns.logger import Logger
from patterns.structural_patterns import AppRoute, Debug



site = Engine()
param_1 = site.get_parameter('Полив')
site.create_parameter(param_1)

param_2 = site.get_parameter('Увлажнение')
site.create_parameter(param_2)

shelf_1 = site.get_shelf('Роза')
site.add_param_in_shelf(shelf_1, param_1)
site.create_shelf(shelf_1, param_1)

shelf_2 = site.get_shelf('Гвоздика')
site.add_param_in_shelf(shelf_2, param_2)
site.create_shelf(shelf_2, param_2)

shelf_3 = site.get_shelf('Фиалка')
site.add_param_in_shelf(shelf_3, param_1)
site.create_shelf(shelf_3, param_1)


logger = Logger('main')

routers = {}


@AppRoute(routes=routers, url='/')
class Index():
    '''
    Контроллер главной страницы фреймворка
    '''
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html')

@AppRoute(routes=routers, url='monitoring/')
class Monitoring:
    '''
    Контроллер страницы монитроинга системы
    '''
    @Debug(name='Monitoring')
    def __call__(self, request):
        return '200 OK', render('monitoring.html')

@AppRoute(routes=routers, url='control/')
class Control:
    '''
    Контроллер страницы управления системы
    '''
    @Debug(name='Control')
    def __call__(self, request):
        method = request['method']
        if method == 'GET':
            print(method, request['request_params'])
        elif method == "POST":
            print(method, request['data'])
            data = decode_data(request['data'])
            print(data)
            site.parameters.append(data['name'])
        return '200 OK', render('control.html',
                model_microcontroller=request.get('microcontroller', None),
                                parameters=site.parameters, shelfs=site.shelfs)

@AppRoute(routes=routers, url='logs/')
class Logs:
    '''
    Контроллер страницы логов системы.
    По умолчанию на настоящую дату
    '''
    @Debug(name='Logs')
    def __call__(self, request):
        date = datetime.datetime.now().strftime('%d %B %Y %H:%M:%S')
        return '200 OK', render('logs.html', date=date)


@AppRoute(routes=routers, url='contacts/')
class Contacts:
    '''
    Контроллер страницы контактов.
    '''
    @Debug(name='Contacts')
    def __call__(self, request):
        method = request['method']
        if method == 'GET':
            print(method, request['request_params'])
        elif method == "POST":
            print(method, request['data'])
        return '200 OK', render('contacts.html')

@AppRoute(routes=routers, url='admin/')
class Admins:
    '''
    Страница управления пользователями
    '''
    @Debug(name='Admins')
    def __call__(self, request):
        pass


@AppRoute(routes=routers, url='create_parameter/')
class NewParamater:
    '''
    Контроллер создания нового параметра
    '''
    @Debug(name='NewParameter')
    def __call__(self, request):
        method = request['method']
        if method == 'GET':
            pass
        elif method == 'POST':
            data = decode_data(request['data'])
            parameter = site.get_parameter(data['name'])
            site.create_parameter(parameter)
        return '200 OK', render('create_parameter.html')


@AppRoute(routes=routers, url='create_shelf/')
class NewShelf:
    '''
    Контроллер для создания новой полки
    '''
    @Debug(name='NewShelf')
    def __call__(self, request):
        if site.parameters:
            method = request['method']
            if method == 'GET':
                pass
            elif method == 'POST':
                data = decode_data(request['data'])
                shelf = site.get_shelf(data['name'])
                param = [i for i in site.parameters if i.name == data['param']][0]
                shelf = site.add_param_in_shelf(shelf, param)
                site.create_shelf(shelf, param)

            return '200 OK', render('create_shelf.html',
                                    params=site.parameters)
        else:
            return '200 OK', render('create_shelf.html')