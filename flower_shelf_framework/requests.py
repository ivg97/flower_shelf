
def parse_input_data(data):
    '''
    Разделение данных запроса
    return: dict
    '''
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            key, value = item.split('=')
            result[key] = value
    return result


class GetRequests:
    '''Работа с get запросами'''

    @staticmethod
    def get_request_params(environ):
        '''
        Получение параметров из запроса
        '''
        query_string = environ['QUERY_STRING']
        request_params = parse_input_data(query_string)
        return request_params


class PostRequests:
    '''Работа с post запросами'''

    @staticmethod
    def get_wsgi_input_data(environ):
        '''

        '''
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if \
            content_length > 0 else b''

        return data


    def parse_wsgi_input_data(self, data):
        '''

        '''
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        '''

        '''
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data


