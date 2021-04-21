from console import Console
from player import Player
from dealer import dealer

class game:
    
    def __init__(self):
        self.__player_list = []
        self.__dealer = dealer()
        self.__console = Console()
    @property
    def player_list(self):
        return self.__player_list
    @property
    def dealer(self):
        return self.__dealer
    @property
    def console(self):
        return self.__console

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
            raise ValueError("Remember that you can only start the game with 3 or 4 players")


    def show_people(self):
        print("\nPlayer list:")
        for (i, _) in enumerate(self.player_list):
            print(f"{i}: {self.player_list[i].name} - "
            +f"{self.player_list[i].money} coins - "
            +f"{len(self.player_list[i].hand)} cards")
        print(f"The dealer have {len(self.dealer.deck)} cards")


    def turn(self,player):
        while True:
            print(f'\n{player.name} Turn!:')
            self.show_people()
            print('Dead Cards:')
            select = self.console.print_turn_menu()
            if select == 0:
                print(player.look_at_the_hand())
            elif select == 1:
                select2 = self.console.print_general_action_menu()
                if select2==0:

                    pass #coup/hit
                elif select2==1:
                    player.income(player)
                    pass #income
                elif select2==2:
                    pass #Foreign aid
                break
            elif select==2:
                select2=self.console.print_character_action_menu()
                if select2==0:
                    pass #Duke tax
                elif select2==1:
                    pass #Assassin murder
                elif select2==2:
                    pass #Captain Extorsion
                elif select2==3:
                    pass #ambassador change
                break



