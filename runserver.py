from flower_shelf_framework.main import Flower_shelf
from urls import fronts
from views import routers
from wsgiref.simple_server import make_server


application = Flower_shelf(routers, fronts)


with make_server('', 8000, application) as httpd:
    print('Сервер запущен на порту 8000..')
    httpd.serve_forever()
