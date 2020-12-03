from virus import Virus
from bacterium import Bacterium
import random
from singl import Singleton

class Simulation(metaclass=Singleton):
    def __init__(self):
        self.organisms = []

    def step(self,x,y):
        for organism in self.organisms:
            i=organism.step(x,y)
            
            if self.search(i,True):
                if None!=organism.get_h()<=0 :
                    self.remove(organism) 
                    continue   
                elif organism.get_h()==None:
                    if random.randint(0,100)<=5 : 
                        z=organism.get()  
                        organism.se(i[0],i[1])
                        self.add(Bacterium(z[0],z[1])) 
                        continue                       
                else:
                    if self.eat(organism,x,y):
                        continue
                
                organism.se(i[0],i[1])
                
                    
                
    def search(self,x,i):
        if i :   
            for organism in self.organisms:
                if organism.get()==x:
                    return False
            return True
        else:
            for organism in self.organisms:
                c=organism.get()
                if c[0]==x[0] and c[1]==x[1]:
                    return organism
            return 
    def add(self,s):
        for i in self.organisms:
            if i==s:
                return
        self.organisms.append(s)
    def getItems(self):
        return self.organisms
    def remove(self,n):
        self.organisms.remove(n)
    def eat(self,o,x,y):
        b=o.get()
        for i in range (-1,2):   
            for j in range (-1,2):
                b[0]-=i
                b[1]-=j
                if 0<b[0]<=x and 0<=b[1]<y: 
                    search=self.search(b,False)
                    if search!=None :        
                        if search.get_h()==None: 
                            z=search.get()
                            self.remove(search)
                            o.se(z[0],z[1])
                            o.set_h()
                            if random.randint(0,100)<=40 :
                                self.add(Virus(b[0],b[1],10)) 
                            return True
                b=o.get()