from sqlalchemy import Column, Integer, String
from models.database import Base

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key = True)
    course_name = Column(String(100), nullable = False)
    credit_hours = Column(Integer, nullable = False)
    instructor = Column(String(100), nullable = False)
    
