import quopri
from flower_shelf_framework.requests import GetRequests, PostRequests


class PageNotFound404:
    '''
    Страница не найдена, 404.
    '''

    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Flower_shelf:
    '''
    Основной файл фреймворка
    '''

    def __init__(self, routers, fronts):
        '''
        Выполняется во время инициализации вновь созданного экземпляра
        класса Flower_shelf
        '''
        self.routers_list = routers
        self.fronts_list = fronts

    def __call__(self, environ, start_response):
        '''
        Выполняется во время вызове экземпляра класса Flower_shelf
        param: environ
        param: start_response

        Получает оставшую часть пути URL-адреса, находит контроллер по
        полученному адресу. Собирает данные в словарь request и запускает
        контроллер с передачей ему словаря request.
        Если контроллер по полученному пути не найден, то запускает контроллер
        PageNotFound404.
        '''

        url_path = environ['PATH_INFO']


        if url_path.startswith('/'):
            url_path = url_path.lstrip('/')

        if not url_path.endswith('/'):
            url_path = f'{url_path}/'


        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params


        if url_path in self.routers_list:
            view = self.routers_list[url_path]
        else:
            view = PageNotFound404()

        for front in self.fronts_list:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


    @staticmethod
    def decode_value(data):
        '''

        '''
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '='), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data
