
from organism import Organism

import random

class Virus(Organism):
    def __init__(self):
        self.__virus=[]
    
    def print(self):
        print(self.__virus)
    def len(self):
        return len(self.__virus)
    def edit(self,s):
        for i in self.__virus:
            if i==s:
                return
        self.__virus.append(s)
    def get(self):
        return self.__virus
    def dell(self,s):
        for i in self.__virus:
            if i==s:
                self.__virus.remove(s)
    def search(self,s):
        for i in self.__virus:
            if i==s:
                return False 
        return True
    def step(self,i,x1,y1):   
        x=i[0]+random.randint(-1,1)
        y=i[1]+random.randint(-1,1)
        if 0<x<=x1 and 0<=y<y1:
            i[0]=x
            i[1]=y
        return 
