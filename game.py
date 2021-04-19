from player import Player
from dealer import dealer

class game:
    def __init__(self):
        self.__player_list = []
        self.__dealer = dealer()
    @property
    def player_list(self):
        return self.__player_list
    @property
    def dealer(self):
        return self.__dealer

    def create_person(self):
        name = input("Enter players name: ")
        money = 2
        PJ=Player(name,money)
        self.dealer.deal_card(PJ)
        self.dealer.deal_card(PJ)
        self.player_list.append(PJ)

        
    def start_game(self):
        if 3 <= len(self.player_list) <= 4:
            return True

        else:
            raise ValueError("Remember that you can only Start the game with 3 or 4 players")


    def show_people(self):
        print("\nPlayer list:")
        for (i, _) in enumerate(self.player_list):
            print(f"{i}: {self.player_list[i].name} - "
            +f"{self.player_list[i].money} coins - "
            +f"{len(self.player_list[i].hand)} cards")
        print(f"The dealer have {len(self.dealer.deck)} cards")

    def print_turn_menu(self):
         print("Select an option: ")
         print("0. Look at your hand ")
         print("1. General action ")
         print("2. Select a card ")
         return int(input())

    def turn(self,player):
        print(f'\n{player.name} Turn!:')
        self.show_people()
        print('Dead Cards:')
        '''
        string= '['                                         #no puedo probar esto todavia :/
        for i in range(len(self.dealer.dead_deck)):
            string+=f'{self.dealer.dead_deck[i].type},'
        string+=']'
        print(string)
        '''
        self.print_turn_menu()




