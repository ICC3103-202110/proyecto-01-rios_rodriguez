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

    def hit(self, player):
        player.plus_money(-7)
        print("Who do you want to hit?")
        for (i, _) in enumerate(self.player_list):
            if self.player_list[i] == player:
                continue
            else:
                print(f"{i}: {self.player_list[i].name}")
        question = int(input("(Select (0,1,2): "))
        print(f"\n The player {self.player_list[question].name} has to turn up a card")
        j = 0
        for i in self.player_list[question].hand:
            print(j,":", i.type)
            j += 1
        
        answer = int(input("Select an option (0/1): "))
        self.dealer.dead_deck.append(self.player_list[question].hand[answer])
        self.player_list[question].hand.pop(answer)
        print(self.player_list[question].hand[answer].type)
        print(self.dealer.dead_deck[0].type)

    



    def income(self, player):
        player.plus_money(1)

    def foreign_aid(self, player):
        player.plus_money(2)

    def duke_tax(self, player):
        player.plus_money(3)


    def turn(self,player):
        while True:
            print(f'\n{player.name} Turn!:')
            self.show_people()
            print('Dead Cards:')
            self.dealer.print_dead_deck()
            select = self.console.print_turn_menu()
            if select == 0:
                print(player.look_at_the_hand())
            elif select == 1:
                select2 = self.console.print_general_action_menu()
                if select2==0:
                    self.hit(player)
                    pass #coup/hit
                elif select2==1:

                    self.income(player)

                    pass #income
                elif select2==2:
                    self.foreign_aid(player)
                    pass #Foreign aid
                break
            elif select==2:
                select2=self.console.print_character_action_menu()
                if select2==0:
                    player.duke_tax(player)
                    pass #Duke tax
                elif select2==1:
                    pass #Assassin murder
                elif select2==2:
                    pass #Captain Extorsion
                elif select2==3:
                    pass #ambassador change
                break



