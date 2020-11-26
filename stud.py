from abc import ABCMeta, abstractmethod
class Menu_item(metaclass=ABCMeta):
    def __init__(self,title):
        self.__title = title

    @abstractmethod
    def run(self): 
        pass
    
    def get_title(self):
        return self.__title

class Menu(Menu_item):
    def __init__(self,title = '',f = True):    
        super().__init__(title)  
        self.__list = []
        self.__f = f
    def run(self):
        while True:
            self.pri()                
            x = self.inp()            
            if x == len(self.__list)+1:                
                break
            self.__list[x-1].run()
    def pri(self):
        for i in range(len(self.__list)):
                print(f'{i+1}.{self.__list[i].get_title()}')
        if self.__f :
            print(f'{len(self.__list)+1}.Выход')            
        else:
            print(f'{len(self.__list)+1}.Возврат')
   
    def addItems(self,title,test):
        item = Simple_menu_item(title,test)
        self.__list.append(item)
        return item

    def addSubMenu(self,title):
        submenu = Menu(title,False)
        self.__list.append(submenu)
        return submenu

    def inp(self): 
        while True:
            x=input("Введите номер пункта ")
            try:
                x = int(x)
                if x>0 or x<=len(self.__list)+1:
                    break
                else: 
                    print(f'Введите число от {1} до {len(self.__list)+1}')
            except:
                print("Error") 
                               
        return x

class Simple_menu_item(Menu_item):
    def __init__(self,title,test):       
        super().__init__(title)
        self.__test = test
    def run(self):
        self.__test()

def test():
    print('Hello World')

class Student():
    def __init__(self, last_name, first_name,middle_name , group, marks):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.group = group
        self.marks =marks 
    def printLong(self): 
        print(f'Фамилия:{self.last_name}\nИмя:{self.first_name}\nОтчество:{self.middle_name}\nГруппа:{self.group}\n')
        print('Оценки:')
        for i in self.marks:
            print(i,':',self.marks[i])

    def printShort(self):
        print(f'Фамилия:{self.last_name}\nИмя:{self.first_name}\nОтчество:{self.middle_name}\nГруппа:{self.group}')
        
    def printSubjects(self):
        print()
        print('Оценки:')
        for i in self.marks:
            print(i,':',self.marks[i])
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
        
    def removeStudentsNumber(self,number):
        del self.__students[number]
        
    def removeStudents(self,student):
        self.__students.remove(student)

    def getStudent(self,number):
        return self.__students[number]

    def getStudentsCount(self):
        return len(self.__students)



if __name__ == "__main__":
    student = Student('иванов','Иван','иванович','34',{'химия': 5,'математика':5})
    # student1 = Student('Потапов','Игрорь','Владимирович',{'физика':2,'информатика':3})
    # student2 = Student('Максимов','Максим','Максимович',{'физика':4,'информатика':4})
    studentRegistry = StudentRegistry()
    studentRegistry.addStudents(student)
    # studentRegistry.addStudents(student1)
    # studentRegistry.addStudents(student2)
    student.printLong()

main_menu = Menu()

file_menu = main_menu.addItems('Список студентов',test)
file_menu = main_menu.addItems('Добавить студента',test)
file_menu = main_menu.addSubMenu('Редактировать студента')

file_menu.addItems('Изменить фамилию', test)
file_menu.addItems('Изменить имя', test)
file_menu.addItems('Изменить отчество', test)
file_menu.addItems('Изменить группу', test)
file_menu.addItems('Добавить оценку', test)
file_menu.addItems('Изменить оценку', test)
file_menu.addItems('Удалить оценку', test)

file_menu = main_menu.addItems('Удалить студента',test)

file_menu = main_menu.addItems('Показать отличников',test)
file_menu = main_menu.addItems('Показать неуспевающих',test)


main_menu.run()