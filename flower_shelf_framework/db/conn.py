from sqlalchemy.orm import sessionmaker
from .declaration import engine, User


session = sessionmaker(bind=engine)


user = User('admin', 'ivan', 'gavr', 'email', 'admin')
session.add(user)