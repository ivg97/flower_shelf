import copy
import quopri


class User:
    def __init__(self, name):
        self.name = name



class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        Engine().admin.append(name)



class Guest(User):
    def __init__(self, name):
        super().__init__(name)
        Engine().guest.append(name)


class UserFactory:
    types = {
        'admin': Admin,
        'guest': Guest,
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


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
        self.admin = []
        self.guest = []
        self.shelfs = []
        self.parameters = []

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create(type_, name)


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



def decode_data(data):
    '''

    '''
    new_data = {}
    for key, value in data.items():
        val = bytes(value.replace('%', '='), 'UTF-8')
        val_decode_str = quopri.decodestring(val).decode('UTF-8')
        new_data[key] = val_decode_str.replace('+', ' ')
    return new_data