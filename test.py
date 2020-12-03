from abc import ABCMeta, abstractmethod

class Organism(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def step(self):
        pass
   
    
class Bacterium(Organism):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getBact(self):
        return self.x,self.y

    def step(self):
        pass



class Simulation():
    def __init__(self):
        self.organisms = []

    def step(self):
        for orgranism in self.organisms:
            organism.step()
    
    def addItems(self,i):
        # for i in self.organisms:
        #     print(i.get())
        self.organisms.append(i)
    def get(self):
        return self.organisms[0]        

s=Simulation()

s.addItems(Bacterium(3,2))

f=s.get()
print(f.getBact())