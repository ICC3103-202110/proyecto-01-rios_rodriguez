from card import card
from player import Player
from random import shuffle
class dealer:
    def __init__(self):
        self.__deck = [card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('Contessa'),
                     card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('Contessa'),
                     card('Duke'),card('Assassin'),card('Captain'),card('Ambassador'),card('Contessa') ] 
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

d=dealer()
d.deck_shuffle()
p=Player('ismael',5)
d.deal_card(p)
d.deal_card(p)
d.deal_card(p)
print('')
#p.look_at_the_hand()
#print(p.hand[0].type)
#print(p.hand[1].type)

