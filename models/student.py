from sqlalchemy import Column, Integer, String
from models.database import Base

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False)
    contact = Column(String(15))
    address = Column(String(255)) 
