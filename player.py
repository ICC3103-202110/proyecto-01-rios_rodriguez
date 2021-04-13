class Player:
    def __init__(self,name, money):
        self.__name = name
        self.__money = money 
        self.__hand = []
    @property
    def name(self):
        return self.__name
    @property
    def money(self):
        return self.__money
    @property
    def hand(self):
        return self.__hand
