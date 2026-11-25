# Student Course Management System

A Python & SQLAlchemy ORM based relational database management project using SQLite. It models many-to-many relationships between students and courses through an enrollment system.

## Database Models
- **Student (`students`)**: Stores student details.
- **Course (`courses`)**: Stores course information.
- **Enrollment (`enrollments`)**: Junction table linking students and courses with enrollment dates and grades.

## Project Structure
```text
student_course_management/
├── models/
│   ├── database.py
│   ├── student.py
│   ├── course.py
│   └── enrollment.py
├── main.py
└── requirements.txt