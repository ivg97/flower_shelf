from views import Index, Monitoring, Control, Logs, Contacts
from flower_shelf_framework.settings import MICROCONTROLLER, COM_PORT


def key(request):
    request['key'] = 'key'

def microcontroller(request):
    request['microcontroller'] = MICROCONTROLLER

def com_port(request):
    request['com_port'] = COM_PORT



fronts = [key, microcontroller]

routers = {
    '/': Index(),
    'monitoring/': Monitoring(),
    'control/': Control(),
    'logs/': Logs(),
    'contacts/': Contacts(),
}