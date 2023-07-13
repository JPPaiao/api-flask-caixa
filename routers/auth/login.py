from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from connection_db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(55))
    password = Column(String(55))
    email = Column(String(55))
    number = Column(Integer)

user = User(username='Lucas', password='1234', email='test@gmail.com', number=1234567)
Session = sessionmaker(bind=engine)
session = Session()

session.add(user)
session.commit()

