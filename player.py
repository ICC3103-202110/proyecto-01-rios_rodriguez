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

    def look_at_the_hand(self):
        print('Your cards are:')
        j=0
        for i in self.hand:
            print(j,i.type)
            j+=1



    def income():
        print("hola") 
        #return self.player_list[player].money + 1

    def foreign_aid():
        return self.player_list[contador].money + 2

    def duke_tax():
        return self.player[contador].money + 3

    def assassin_murder():
        print("You have to turn one of your cards")

        pass

        self.player[contador].money - 3
        pass

    def captain_extortion():
        pass

    def ambassador_change():
        pass

    def duke_stop_foreign_aid():

        pass

    def contessa_stop_murder():
        pass

    def ambassador_or_captain_stop_extortion():
        pass



    









