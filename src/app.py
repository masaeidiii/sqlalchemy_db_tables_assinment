from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///school.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', back_populates='student') 

class Course(Base):
    
    __tablename__ = 'courses' 
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    unit = Column(Integer)
    # خط 21.22 مهمن برای وصل شدن به 14 
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='courses')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()


# s1 = Student(name='Ali')
# s2 = Student(name='Sara')

# c1 = Course(title='Math', unit=3, student=s1) 
# c2 = Course(title='Physics', unit=4, student=s1)
# c3 = Course(title='Art', unit=2, student=s2)

#sessionLocal.add_all([s1, s2, c1, c2, c3])

#sessionLocal.commit()


# temp_student = sessionLocal.query(Course).filter_by(id=2).first() 
# print(temp_student.student.name)

# temp_student = sessionLocal.query(Student).filter_by(id=2).first() 
# print(temp_student.name)


# for course in temp_student.courses:
#     print(course.unit)

# update
# temp_student.name = "samane"
# sessionLocal.commit()