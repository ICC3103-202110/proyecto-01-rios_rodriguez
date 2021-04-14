from card import card
from player import Player
from random import shuffle
class dealer:
    def __init__(self):
        self.__deck = [card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('contessa'),
                     card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('contessa'),
                     card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('contessa') ] 
        self.__dead_deck = list()
    @property
    def deck(self):
        return self.__deck
    @property
    def dead_deck(self):
        return self.__dead_deck
    def deck_shuffle(self):
        shuffle(self.deck)
        return self.deck

    def deal_card(self,Player):
        Player.hand.append(self.deck[0])
        self.deck.pop(0)

    def move_card_to_dead():
        pass
'''
d=dealer()
d.deck_shuffle()
p=Player('ismael',5)
j=0
for i in d.deck:
    print(j,i.type)
    j+=1
d.deal_card(p)
print('')
j=0
for i in d.deck:
    print(j,i.type)
    j+=1
#print(p.hand[0].type)'''