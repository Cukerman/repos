from menu import Menu
from simpleMenu import Simple_menu_item
from menuItem import Menu_item
from studentRegistry import StudentRegistry
from edit import Edit
from student import Student
from achieverVisitor import (
    LowArchieverVisitor,
    HightArchieverVisitor
    )
from printVisitor import (
    BriefPrintVisitor,
    DetailedPrintVisitor
    ) 


def showHighAchiversCommand():
    StudentRegistry().visit_students(HightArchieverVisitor())
def showLowArchiversCommand():
    StudentRegistry().visit_students(LowArchieverVisitor())
def listStudentCommand():
    StudentRegistry().visit_students(DetailedPrintVisitor())
def addStudent():   
    StudentRegistry().addStudents(Student(input('Введите Фамилию: '),input('Введите Имя: '),input('Введите Отчество: '),input('Введите группу: ')))
    StudentRegistry().save()
def removeStudent():
    studentRegistry.visit_students(BriefPrintVisitor()) 
    if StudentRegistry().getStudentsCount() != 0:
        while True: 
            n = int(input('Введите номер ученика '))-1
            if StudentRegistry().getStudentsCount()> n>=0:
                break
            print ('error')
        while True:    
            p = input(f'Удалить ученика {n+1}?\n1.Да\n2.нет\n')
            if p=='2' or p == '1' or p== 'да' or p== 'Да' or p=='Нет' or p== 'нет':
                break
            else:    
                print ('error')
        if p == '1' or p== 'да' or p== 'Да':
            StudentRegistry().removeStudentsNumber(n-1) 
            print('Вы удалили студента')
            studentRegistry.save()
def SelectS():
    if StudentRegistry().getStudentsCount()!=0:
        studentRegistry.visit_students(BriefPrintVisitor()) 
        while True: 
            n = int(input('Введите номер ученика '))-1
            if StudentRegistry().getStudentsCount()> n>=0:
                break
            print ('error')
        Edit().student = StudentRegistry().getStudent(n)
    else:
        return True
        
def ShowS():
    if StudentRegistry().getStudentsCount()!=0:    
        Edit().student.printLong()
        StudentRegistry().save()    
        test()
def DeselectS():
    if StudentRegistry().getStudentsCount()!=0:
        Edit().student = None
def EditF() :
    Edit().student.first_name = input('Введите Имя: ')
def EditL():
    Edit().student.last_name = input('Введите Фамиллию: ')
def EditM():
    Edit().student.middle_name = input('Введите Отчество: ')
def EditG():
    Edit().student.group = input('Введите Группу: ')
def EditMark():
    if len(Edit().student.marks) == 0:
        print('Оценок нет')
    else:
        Edit().student.printSubjects()       
        n = input('Введите название предмета: ')
        if n not in Edit().student.marks:
            print("Такого предмента нет")
            return
        Edit().student.marks[n] = int(input('Введите оценку: '))
      
def AddMark():
    с=input('Введите название предмета: ')
    Edit().student.marks[с] = int(input('Введите оценку: '))
def RemoveMark():
    if len(Edit().student.marks) == 0:
        print('Оценок нет')
    else:
        Edit().student.printSubjects()       
        n = input('Введите название предмета: ')
        if n not in Edit().student.marks:
            print("Такого предмента нет")
            return
        while True:    
            p = input(f'Удалить оценку {n}?\n1.Да\n2.нет\n')
            if p=='2' or p == '1' or p== 'да' or p== 'Да' or p=='Нет' or p== 'нет':
                break
            else:    
                print ('error')
        if p == '1' or p== 'да' or p== 'Да':
            del Edit().student.marks[n]
            print('Вы удалили оценку')
    pass
def test():
    print('Студентов нет')




if __name__ == '__main__':
    studentRegistry = StudentRegistry()
    # student = Student('Иванов','Иван','Иванович','34',{'химия': 5,'математика':5})
    # student1 = Student('Потапов','Игрорь','Владимирович','32',{'физика':3,'информатика':5})
    # student2 = Student('Максимов','Максим','Максимович','11',{'физика':4,'информатика':4})
    # studentRegistry.addStudents(student)
    # studentRegistry.addStudents(student1)
    # studentRegistry.addStudents(student2)
    studentRegistry.load()
    main_menu = Menu()

    file_menu = main_menu.addItems('Список студентов',listStudentCommand)
    file_menu = main_menu.addItems('Добавить студента',addStudent)
    
    file_menu = main_menu.addSubMenu('Редактировать студента')

    file_menu.Select(SelectS)
    file_menu.Show(ShowS)
    file_menu.Deselect(DeselectS)

    file_menu.addItems('Изменить фамилию', EditL)
    file_menu.addItems('Изменить имя', EditF)
    file_menu.addItems('Изменить отчество', EditM)
    file_menu.addItems('Изменить группу', EditG)
    file_menu.addItems('Добавить оценку', AddMark)
    file_menu.addItems('Изменить оценку', EditMark)
    file_menu.addItems('Удалить оценку', RemoveMark)
    
     
    file_menu = main_menu.addItems('Удалить студента',removeStudent)

    file_menu = main_menu.addItems('Показать отличников',showHighAchiversCommand)
    file_menu = main_menu.addItems('Показать неуспевающих',showLowArchiversCommand)



    main_menu.run()
    studentRegistry.save()