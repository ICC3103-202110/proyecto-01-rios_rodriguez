class Person:
    def __init__(self,person_id, name):
        self.__name = name
        self.__person_id = person_id
    
    @property
    def name(self):
        return self.__name
    @property
    def person_id(self):
        return self.__person_id
