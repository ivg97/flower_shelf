from flower_shelf.main import Flower_shelf
from urls import routers, fronts
from wsgiref.simple_server import make_server


application = Flower_shelf(routers, fronts)


with make_server('', 8000, application) as httpd:
    print('Сервер запущен на порту 8000..')
    httpd.serve_forever()
