from sqlalchemy import Column, Integer, Date, ForeignKey, String
from models.database import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primarykey = True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    enrollment_date = Column(Date)
    grade = Column(String(2)) 