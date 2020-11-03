from student import Student
from singl import Singleton
import json


class StudentRegistry(metaclass=Singleton):
    def __init__(self):
        self.__students = [] 

    def addStudents(self, student):
        self.__students.append(student)

    def removeStudentsNumber(self,n):
        del self.__students[n]

    def removeStudents(self,n):
        self.__students.remove(n)

    def getStudent(self,n):
        return self.__students[n]

    def getStudentsCount(self):
        return len(self.__students)

    def visit_students(self, visitor):
        visitor.start_visit()
        
        for i, student in enumerate(self.__students):
            visitor.visit_student(i, student)
        
        visitor.finish_visit()
    
    def save(self):
        person = []
        for i in range(StudentRegistry().getStudentsCount()):
            p=StudentRegistry().getStudent(i)
            P={'last_name':p.last_name,'first_name':p.first_name,'middle_name':p.middle_name,'group':p.group,'marks':p.marks}
            person.append(P)
        with open('students.json','w') as f:
            json.dump(person, f)

    def load(self):
        with open('students.json','r') as f:
            f=json.load(f)
            for i in range(0,len(f)):
                StudentRegistry().addStudents(Student(f[i]['last_name'],f[i]['first_name'],f[i]['middle_name'],f[i]['group'],f[i]['marks']))