from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite')

DeclarativeBase = declarative_base()


class UserTable(DeclarativeBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column('username', String)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    email = Column('email', String)
    status = Column('status', String)

    def __init__(self, username, first_name, last_name, email, status):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status

    def __repr__(self):
        return f'{self.username}'


class ParamTable(DeclarativeBase):
    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class ShelfTable(DeclarativeBase):
    __tablename__ = 'shelfs'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


def main():
    DeclarativeBase.metadata.create_all(engine)


def session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


