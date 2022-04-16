import datetime

from flower_shelf_framework.templator import render

class Index():
    '''
    Контроллер главной страницы фреймворка
    '''

    def __call__(self, request):
        return '200 OK', render('index.html')


class Monitoring:
    '''
    Контроллер страницы монитроинга системы
    '''

    def __call__(self, request):
        return '200 OK', render('monitoring.html')

class Control:
    '''
    Контроллер страницы управления системы
    '''

    def __call__(self, request):
        return '200 OK', render('control.html',
                model_microcontroller=request.get('microcontroller', None))

class Logs:
    '''
    Контроллер стрницы настроек системы.
    По умолчанию на настоящую дату
    '''

    def __call__(self, request):
        date = datetime.datetime.now().strftime('%d %B %Y %H:%M:%S')
        return '200 OK', render('logs.html', date=date)


class Contacts:
    '''
    Контроллер стрницы контактов.
    '''

    def __call__(self, request):
        method =  request['method']
        if method == 'GET':
            print(method, request['request_params'])
        elif method == "POST":
            print(method, request['data'])
        return '200 OK', render('contacts.html')
