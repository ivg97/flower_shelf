import copy
import quopri

from flower_shelf_framework.db import declaration

from patterns.logs import Log


session = declaration.session()


class User:

    def __init__(self, username, **kwargs):

        self.username = username
        self.last_name = kwargs['last_name']
        self.first_name = kwargs['first_name']
        self.email = kwargs['email']
        self.status = kwargs['status']

        new_user = declaration.UserTable(username=self.username,
                                         first_name=self.first_name,
                                         last_name=self.last_name,
                                         email=self.email,
                                         status=self.status)
        session.add(new_user)
        session.commit()


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

    def __init__(self, name):
        self.name = name
        self.shelf = []

        new_param = declaration.ParamTable(name=self.name)
        session.add(new_param)
        session.commit()


class Shelf:

    def __init__(self, name, parameter=None):
        self.parameter = parameter
        self.name = name

        new_shelf = declaration.ShelfTable(name=self.name)
        session.add(new_shelf)
        session.commit()


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

    @staticmethod
    def create_parameter(name):
        return Parameter(name)

    @staticmethod
    def create_shelf(name):
        return Shelf(name)

    def all_users(self):
        return session.query(declaration.UserTable)

    @staticmethod
    def all_param():
        return session.query(declaration.ParamTable)

    def all_shelf(self):
        return session.query(declaration.ShelfTable)

    @staticmethod
    def create_log(log):
        return Log(log)

    def start_db(self):
        declaration.main()




def decode_data(data):
    '''

    '''
    new_data = {}
    for key, value in data.items():
        val = bytes(value.replace('%', '='), 'UTF-8')
        val_decode_str = quopri.decodestring(val).decode('UTF-8')
        new_data[key] = val_decode_str.replace('+', ' ')
    return new_data