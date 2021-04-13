class Person:
    def __init__(self,name, money):
        self.__name = name
        self.__money = money 
       
    @property
    def name(self):
        return self.__name
    @property
    def money(self):
        return self.__money
        
   
    
