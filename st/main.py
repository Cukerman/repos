from menu import Menu
from simpleMenu import Simple_menu_item
from menuItem import Menu_item
from studentRegistry import StudentRegistry
from student import Student
from achieverVisitor import (
    LowArchieverVisitor,
    HightArchieverVisitor)
from printVisitor import (BriefPrintVisitor,DetailedPrintVisitor)

def showHighAchiversCommand():
    studentRegistry.visit_students(HightArchieverVisitor())
def showLowArchiversCommand():
    studentRegistry.visit_students(LowArchieverVisitor())
def listStudentCommand():
    studentRegistry.visit_students(DetailedPrintVisitor())
def addStudentCommand():
    
    studentRegistry.addStudents(Student(input('Введите Фамилию: '),input('Введите Имя: '),input('Введите Отчество: '),input('Введите группу: ')))

def test():
    print('Hello World')
if __name__ == '__main__':
    student = Student('Иванов','Иван','Иванович','34',{'химия': 5,'математика':5})
    student1 = Student('Потапов','Игрорь','Владимирович','32',{'физика':2,'информатика':5})
    student2 = Student('Максимов','Максим','Максимович','11',{'физика':4,'информатика':4})
    studentRegistry = StudentRegistry()
    studentRegistry.addStudents(student)
    studentRegistry.addStudents(student1)
    studentRegistry.addStudents(student2)

main_menu = Menu()

file_menu = main_menu.addItems('Список студентов',listStudentCommand)
file_menu = main_menu.addItems('Добавить студента',addStudentCommand)
file_menu = main_menu.addSubMenu('Редактировать студента')

file_menu.addItems('Изменить фамилию', test)
file_menu.addItems('Изменить имя', test)
file_menu.addItems('Изменить отчество', test)
file_menu.addItems('Изменить группу', test)
file_menu.addItems('Добавить оценку', test)
file_menu.addItems('Изменить оценку', test)
file_menu.addItems('Удалить оценку', test)

file_menu = main_menu.addItems('Удалить студента',test)

file_menu = main_menu.addItems('Показать отличников',showHighAchiversCommand)
file_menu = main_menu.addItems('Показать неуспевающих',showLowArchiversCommand)



main_menu.run()