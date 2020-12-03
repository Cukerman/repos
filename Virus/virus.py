
from organism import Organism

import random

class Virus(Organism):
    def __init__(self,x,y,h=10):
        self.x = x
        self.y = y
        self.h = h
    def get(self):
        a=[]
        a.append(self.x)
        a.append(self.y)
        return a
    def color(self):
        return 'red'
    def step(self,x1,y1):   
        x=self.x+random.randint(-2,2)
        y=self.y+random.randint(-2,2)
        self.h-=1
        if 0<x<=x1 and 0<=y<y1:
            return x,y
        return self.get()    
    def se(self,i,j):
        if self.h>0:
            self.x = i
            self.y = j
    def get_h(self):
        return self.h
    def set_h(self):
        self.h = 10