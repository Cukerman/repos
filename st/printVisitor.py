from studentVisit import StudentVisitor


class BriefPrintVisitor(): 
    def start_visit(self):       
        self.__students = True
  
    def visit_student(self, n, student): 
        print(f"{n+1}. ", end="")
        student.printShort()
        self.__students = False
 
    def finish_visit(self):
        if self.__students:
            print('Студентов нет')

class DetailedPrintVisitor():
    def start_visit(self):       
        self.__students = True
  
    def visit_student(self, n, student): 
        print(f'===={n+1}====')
        student.printLong()
        self.__students = False
 
    def finish_visit(self):
        if self.__students:
            print('Студентов нет')