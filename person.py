class Person:
    def _init_(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
