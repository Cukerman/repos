from abc import ABCMeta, abstractmethod

class Menu_item(metaclass=ABCMeta):
    def __init__(self,title):
        self.__title = title

    @abstractmethod
    def run(self): 
        pass
    
    def get_title(self):
        return self.__title