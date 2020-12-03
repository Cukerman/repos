from organism import Organism

import random

class Bacterium(Organism):
    def __init__(self):
        self.__bact=[]
    def step(self):
        pass
    def print(self):
        print(self.__bact)
    def edit(self,s):
        for i in self.__bact:
            if i==s:
                return
        self.__bact.append(s)
    def get(self):
        return self.__bact

    def dell(self,s):
        for i in self.__bact:
            if i==s:
                self.__bact.remove(s)
    def search(self,s):
        for i in self.__bact:
            if i==s:
                return False
        return True