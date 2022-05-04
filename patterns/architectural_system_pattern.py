
class User:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor
        self.tablename = 'users'

    def all(self):
        statement = f'select * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            user = User(name)
            user.id = id
            result.append(user)
        return result

    def insert(self, object):
        statement = f'insert into {self.tablename} (name) values (?)'
        self.cursor.execute(statement, (object.name,))
        try:
            self.connection.commit()
        except Exception as err:
            raise Exception(err.args)