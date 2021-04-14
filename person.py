class Person:
    def __init__(self,name, money, deck):
        self.__name = name
        self.__money = money 
        self.__deck = deck
       
    @property
    def name(self):
        return self.__name
    @property
    def money(self):
        return self.__money
    @property 
    def deck(self):
        return self.__deck
        
   
    
