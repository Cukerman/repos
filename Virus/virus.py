from singl import Singleton
from cells import Cells


class Virus(metaclass=Singleton):
    def __init__(self):
        self.__virus=[]

    def add(self,cells):
        self.__virus.append(cells)
    
    def get(self, n):
        return self.__virus[n]
    
    def getCount(self):
        return len(self.__virus)
    
    def edit(self,n,ed):
        print(self.__virus[n])  
        k=[]
        k.append(ed)
        k.append(self.__virus[n][1])
        k.append(self.__virus[n][2])
        self.__virus[n]=k