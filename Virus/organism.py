from abc import ABCMeta, abstractmethod

class Organism(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def step(self):
        pass
    @abstractmethod
    def print(self):
        pass
    