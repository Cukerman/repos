
from organism import Organism

import random

class Virus(Organism):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get(self):
        return self.x,self.y
    def color(self):
        return 'red'
    def step(self,i,x1,y1):   
        x=i[0]+random.randint(-1,1)
        y=i[1]+random.randint(-1,1)
        if 0<x<=x1 and 0<=y<y1:
            i[0]=x
            i[1]=y
        return 
