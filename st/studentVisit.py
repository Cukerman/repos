
from abc import ABCMeta, abstractmethod

class StudentVisitor(metaclass=ABCMeta):
    @abstractmethod
    def startVisit(self): 
        pass
    
    @abstractmethod
    def visitStudent(self, number, student): 
        pass
    @abstractmethod
    def finishVisit(self): 
        pass