from card import card
from player import Player
import random
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
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self,Player):
        num= random.randint(0,len(self.deck)-1)
        Player.hand.append(self.deck[num])
        self.deck.pop(num)

    def print_dead_deck(self):
        for i in self.dead_deck:
            print(i.type)

