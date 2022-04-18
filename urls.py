from views import Index, Monitoring, Control, Logs, Contacts, NewParamater, NewShelf
from flower_shelf_framework.settings import MICROCONTROLLER, COM_PORT


def key(request):
    request['key'] = 'key'

def microcontroller(request):
    request['microcontroller'] = MICROCONTROLLER

def com_port(request):
    request['com_port'] = COM_PORT



fronts = [key, microcontroller, com_port]

# routers = {
#     '/': Index(),
#     'monitoring/': Monitoring(),
#     'control/': Control(),
#     'logs/': Logs(),
#     'contacts/': Contacts(),
#     'create_parameter/': NewParamater(),
#     'create_shelf/': NewShelf(),
# }