from views import Index, Monitoring, Control, Logs, Contacts
from flower_shelf.settings import MICROCONTROLLER


def key(request):
    request['key'] = 'key'

def microcontroller(request):
    request['microcontroller'] = MICROCONTROLLER



fronts = [key, microcontroller]

routers = {
    '/': Index(),
    'monitoring/': Monitoring(),
    'control/': Control(),
    'logs/': Logs(),
    'contacts/': Contacts(),
}