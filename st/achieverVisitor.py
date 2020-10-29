from studentVisit import StudentVisitor
from studentRegistry import StudentRegistry
class HightArchieverVisitor():
    def start_visit(self):
        self.__students = True

    def visit_student(self, number, student):       
        c=0
        k=0
        for mark in list(student.marks.values()):
            c+=mark
            k+=1
        if c == k*5 and c!=0:
            print(f'===={number+1}====')
            student.printLong() 
            self.__students = False

    def finish_visit(self):
        if self.__students:
            print('Отличники нет')
            
class LowArchieverVisitor():
    def start_visit(self):
        self.__students = True

    def visit_student(self, number, student):
        for mark in list(student.marks.values()):
            if mark < 3:
                print(f'===={number+1}====')
                student.printLong()
                self.__students = False

    def finish_visit(self):
        if self.__students:
            print('Неуспевающих нет')

