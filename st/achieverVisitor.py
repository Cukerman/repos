from studentVisit import StudentVisitor

class HightArchieverVisitor():
    def start_visit(self):
        self.__has_students = True

    def visit_student(self, number, student):       
        if sum(list(student.marks.values()))/len(list(student.marks.values())) == 5:
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

