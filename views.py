import datetime

from flower_shelf_framework.templator import render
from patterns.creational_patterns import Engine, decode_data, Parameter
from patterns.logger import Logger
from patterns.structural_patterns import AppRoute, Debug
from patterns.behavioral_patterns import TemplateView, ListView, CreateView



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
        logger.log(site.create_log('Click Index'), site.logs)
        return '200 OK', render('index.html')

@AppRoute(routes=routers, url='monitoring/')
class Monitoring:
    '''
    Контроллер страницы монитроинга системы
    '''
    @Debug(name='Monitoring')
    def __call__(self, request):
        logger.log(site.create_log('Click Monitoring'), site.logs)
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
            logger.log(site.create_log(f'Click Control - method {method}'), site.logs)
            print(method, request['request_params'])
        elif method == "POST":
            logger.log(site.create_log(f'Click Control - method {method}'), site.logs)
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
        logger.log(site.create_log(f'Click Logs'), site.logs)
        return '200 OK', render('logs.html', logs=site.logs[::-1])


@AppRoute(routes=routers, url='contacts/')
class Contacts:
    '''
    Контроллер страницы контактов.
    '''
    @Debug(name='Contacts')
    def __call__(self, request):
        logger.log(site.create_log(f'Click Contacts'), site.logs)
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
        logger.log(site.create_log(f'Click Admins'), site.logs)
        pass

@AppRoute(routes=routers, url='users/')
class ListUsers(ListView):
    template_name = 'users_list.html'



    def get_context_data(self):
        logger.log(site.create_log(f'Click ListUsers'), site.logs)
        context = super().get_context_data()
        context['users'] = site.get_users()
        return context



@AppRoute(routes=routers, url='create_parameter/')
class NewParamater:
    '''
    Контроллер создания нового параметра
    '''
    @Debug(name='NewParameter')
    def __call__(self, request):
        logger.log(site.create_log(f'Click NewParameter'), site.logs)
        method = request['method']
        if method == 'GET':
            pass
        elif method == 'POST':
            data = decode_data(request['data'])
            logger.log(site.create_log(f'Click NewParameter - data: {data}'), site.logs)
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
        logger.log(site.create_log(f'Click NewShelf'), site.logs)
        if site.parameters:
            method = request['method']
            if method == 'GET':
                pass
            elif method == 'POST':
                data = decode_data(request['data'])
                logger.log(site.create_log(f'Click NewShelf - data: {data}'), site.logs)
                shelf = site.get_shelf(data['name'])
                param = [i for i in site.parameters if i.name == data['param']][0]
                shelf = site.add_param_in_shelf(shelf, param)
                site.create_shelf(shelf, param)

            return '200 OK', render('create_shelf.html',
                                    params=site.parameters)
        else:
            return '200 OK', render('create_shelf.html')


@AppRoute(routes=routers, url='create_user/')
class AddUser(CreateView):
    template_name = 'create_user.html'

    def create_object(self, data):

        data = decode_data(data)
        user = data['param']
        username = data['username']
        last_name = data['last_name']
        first_name = data['first_name']
        email = data['email']

        new_user = site.create_user(user, username, last_name=last_name,
                                    first_name=first_name, email=email,
                                    status=user)

        if user == 'admin':
            site.admin.append(new_user)
        elif user == 'guest':
            site.guest.append(new_user)


