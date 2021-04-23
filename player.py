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

    @money.setter
    def money(self, value):
        if value < 0:
            self.money = 0 
        else:
            self.money = value

    def look_at_the_hand(self):
        print('Your cards are:')
        j = 0
        for i in self.hand:
            print(j,":",i.type)
            j += 1
        

    def plus_money(self, value):
        self.__money += value




    









