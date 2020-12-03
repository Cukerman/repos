from organism import Organism

import random

class Bacterium(Organism):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = None
    def get(self):
        a=[]
        a.append(self.x)
        a.append(self.y)
        return a
    def color(self):
        return 'green'
    def step(self,x1,y1):
        x=self.x+random.randint(-1,1)
        y=self.y+random.randint(-1,1)
        if 0<x<=x1 and 0<=y<y1:
            return x,y
        return self.get()
    def se(self,i,j):
        if i!=None:    
            self.x = i
            self.y = j
    def get_h(self):
        return self.h