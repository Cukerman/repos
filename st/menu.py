from menuItem import Menu_item
from simpleMenu import Simple_menu_item


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

