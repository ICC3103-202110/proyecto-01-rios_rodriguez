class Person:
    def __init__(self,name, person_id, money):
        self.__name = name
        self.__person_id = person_id
        self.__money = money
    
    @property
    def name(self):
        return self.__name
    @property
    def person_id(self):
        return self.__person_id

 """       
    @property
    def money(self):
        return self.__money
"""
    