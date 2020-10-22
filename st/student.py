
class Student():
    def __init__(self, last_name, first_name,middle_name , group, marks={}):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.group = group
        self.marks = marks 
    
    def printLong(self):    
        print(f'Фамилия:{self.last_name}\nИмя:{self.first_name}\nОтчество:{self.middle_name}\nГруппа:{self.group}\nОценки:')    
        for i in self.marks:
            print('  ',i,':',self.marks[i])

    def printShort(self):
        print(f'Фамилия:{self.last_name}\nИмя:{self.first_name}\nОтчество:{self.middle_name}\nГруппа:{self.group}')
        
    def printSubjects(self):
        print()
        print('Оценки:')
        for i in self.marks:
            print('   ', i,':',self.marks[i])