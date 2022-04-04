from jinja2 import FileSystemLoader
from jinja2.environment import Environment



def render(template_name, folder='templates', **kwargs):
    '''
    param template_name: имя шаблона
    param folder: имя папки в которой ведется поиск шаблона
    param kwargs: доп параметры
    return: html шаблон

    '''
    env = Environment()
    env.loader = FileSystemLoader(folder)

    template = env.get_template(template_name)
    return template.render(**kwargs)
