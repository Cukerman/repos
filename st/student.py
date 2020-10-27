
class Student():
    def __init__(self, last_name, first_name,middle_name , group, marks=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.group = group
        if marks:
            self.marks = marks
        else:
            self.marks = {}
    
    def printLong(self):    
        print(f'Фамилия:{self.last_name}\nИмя:{self.first_name}\nОтчество:{self.middle_name}\nГруппа:{self.group}\nОценки:')    
        for i in self.marks:
            print('  ',i,':',self.marks[i])

    def printShort(self):
        print(f'{self.last_name} {self.first_name} {self.middle_name} {self.group}')
        
    def printSubjects(self):
        
        for i in self.marks:
            print(i,':',self.marks[i])