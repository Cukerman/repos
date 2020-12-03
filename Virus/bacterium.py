from organism import Organism

import random

class Bacterium(Organism):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get(self):
        return self.x,self.y
    def color(self):
        return 'green'
    def step(self):
        pass
    
