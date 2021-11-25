from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"
    contact_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    number = Column(Integer)


