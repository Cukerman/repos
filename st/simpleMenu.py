from menuItem import Menu_item


class Simple_menu_item(Menu_item):
    def __init__(self,title,test):       
        super().__init__(title)
        self.__test = test
    def run(self):
        self.__test()

def test():
    print('Hello World')