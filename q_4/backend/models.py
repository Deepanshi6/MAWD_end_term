from sqlalchemy import Column ,Integer ,String ,DateTime
from database import Base

class Books(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    title=Column(String,index=True)
    author=Column(String,index=True)
    year=Column(Integer,index=True)