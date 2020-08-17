import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base(object):
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    

