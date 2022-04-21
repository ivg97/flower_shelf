import copy
import quopri

from patterns.logs import Log


class User:
    def __init__(self, username, **kwargs):
        self.username = username
        print(kwargs)

        self.last_name = kwargs['last_name']
        self.first_name = kwargs['first_name']
        self.email = kwargs['email']
        self.status = kwargs['status']




class Admin(User):
    def __init__(self, username, **kwargs):
        super().__init__(username, **kwargs)




class Guest(User):
    def __init__(self, username, **kwargs):
        super().__init__(username, **kwargs)



class UserFactory:
    types = {
        'admin': Admin,
        'guest': Guest,
    }

    @classmethod
    def create(cls, type_, username, **kwargs):
        return cls.types[type_](username, **kwargs)


class ControlPrototype:

    def clone(self):
        return copy.deepcopy(self)


class ControlSettings(ControlPrototype):

    def __init__(self, name, shelf):
        self.shelf = shelf
        self.name = name
        self.shelf.shelfs.appens(self)


class LightingControl(ControlSettings):
    pass


class WateringControl(ControlSettings):
    pass

class HumidificationControl(ControlSettings):
    pass

class ControlFactory:
    types = {
        'lighting': LightingControl,
        'watering': WateringControl,
        'humidification': HumidificationControl,
    }

    @classmethod
    def create(cls, type_, shelf, parameter):
        return cls.types[type_](shelf, parameter)

class Parameter:

    auto_id = 1

    def __init__(self, name):
        self.id = Parameter.auto_id
        Parameter.auto_id += 1
        self.name = name
        self.shelf = []

class Shelf:

    auto_id = 1

    def __init__(self, name, parameter=None):
        self.id = Parameter.auto_id
        Parameter.auto_id += 1
        self.parameter = parameter
        self.name = name

class Engine:
    def __init__(self):
        self.logs = []
        self.admin = []
        self.guest = []
        self.shelfs = []
        self.parameters = []

    @staticmethod
    def create_user(type_, username, **kwargs):
        return UserFactory.create(type_, username, **kwargs)




    def create_parameter(self, name):
        self.parameters.append(name)


    def create_shelf(self, shelf, parameter):
        self.shelfs.append(shelf)
        if parameter != None:
            parameter.shelf.append(shelf)

    @staticmethod
    def get_shelf(name):
        return Shelf(name)

    @staticmethod
    def add_param_in_shelf(shelf, param):
        shelf.parameter = param
        return shelf


    @staticmethod
    def get_parameter(name):
        return Parameter(name)


    def get_users(self):
        return self.admin + self.guest

    @staticmethod
    def create_log(log):
        return Log(log)



def decode_data(data):
    '''

    '''
    new_data = {}
    for key, value in data.items():
        val = bytes(value.replace('%', '='), 'UTF-8')
        val_decode_str = quopri.decodestring(val).decode('UTF-8')
        new_data[key] = val_decode_str.replace('+', ' ')
    return new_data