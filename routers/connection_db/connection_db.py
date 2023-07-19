from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/db_python', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
