from database import Base,engine
from models import Books

Base.metadata.create_all(bind=engine)
#run only once to create database