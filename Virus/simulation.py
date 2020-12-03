from virus import Virus
from bacterium import Bacterium


class Simulation():
    def __init__(self):
        self.organisms = []

    def step(self):
        for orgranism in self.organisms:
            organism.step()
    
    def add(self,s):
        for i in self.organisms:
            if i==s:
                return
        self.organisms.append(s)
    def getItems(self):
        return self.organisms