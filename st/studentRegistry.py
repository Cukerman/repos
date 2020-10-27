from student import Student



class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

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
