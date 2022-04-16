import copy


class User:
    pass


class Admin(User):
    pass


class Guest(User):
    pass


class UserFactory:
    types = {
        'admin': Admin,
        'guest': Guest,
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class ControlPrototype:

    def clone(self):
        return copy.deepcopy(self)


class ControlSettings(ControlPrototype):

    def __init__(self, shelf, parameter):
        self.shelf = shelf
        self.parameter = parameter
        self.parameter.control_settings.appens(self)


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

    auto_id = 0

    def __init__(self, ):
