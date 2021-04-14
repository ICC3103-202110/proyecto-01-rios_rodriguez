
from player import Player
from person import Person

class game:
    def __init__(self):
        self.__player_list = []
    @property
    def player_list(self):
        return self.__player_list

    def create_person(self,dealer):
        name = input("Enter players name: ")
        money = 2
        PJ=Player(name,money)
        dealer.deal_card(PJ)
        dealer.deal_card(PJ)
        self.player_list.append(PJ)

        
    def start_game(self):
        if 3 <= len(self.player_list) <= 4:
            return True
        else:
            raise ValueError("Remember that you can only Start the game with 3 or 4 players")


    def show_people(self,dealer):
        print("\nPeople created:")
        for (i, _) in enumerate(self.player_list):
            print(f"{i}: {self.player_list[i].name} - "
            +f"{self.player_list[i].money} coins - "
            +f"{len(self.player_list[i].hand)} cards")
        print(f"The dealer have {len(dealer.deck)} cards")
            

 