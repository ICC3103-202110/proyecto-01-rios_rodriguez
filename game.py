from console import Console
from player import Player
from dealer import dealer
import random

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
        print(f"\nThe dealer has {len(self.dealer.deck)} cards")

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
        print(self.player_list[question].hand[answer-1].type)
        print(self.dealer.dead_deck[0].type)

    def assassin(self, player):
        player.plus_money(-3)
        print("Who do you want to Assassin?")
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
        print(self.player_list[question].hand[answer-1].type)
        print(self.dealer.dead_deck[0].type)


    def income(self, player):
        player.plus_money(1)

    def foreign_aid(self, player):
        player.plus_money(2)

    def duke_tax(self, player):
        player.plus_money(3)

    def captain_extortion(self, player):
        print("Who do you want to extortion?")
        for (i, _) in enumerate(self.player_list):
            if self.player_list[i] == player:
                continue
            else:
                print(f"{i}: {self.player_list[i].name}")
        question = int(input("(Select (0,1,2): "))
        print(f"\n The player {self.player_list[question].name} will loose 2 coins")
        if self.player_list[question].money == 1:
            self.player_list[question].plus_money(-1)
            player.plus_money(+1)
        else:
            self.player_list[question].plus_money(-2)
            player.plus_money(+2)

    def deal_to_list(self,list):
        num= random.randint(0,len(self.dealer.deck)-1)
        list.append(self.dealer.deck[num])
        self.dealer.deck.pop(num)

    def ambassador_change(self,player):
        Change=[]
        for i in player.hand:
            Change.append(i)
        self.deal_to_list(Change)
        self.deal_to_list(Change)
        j=0
        for i in Change:
            print(j,':',i.type)
            j+=1
        answer= int(input('Select your first card:'))
        answer2= int(input('Select your second card:'))
        player.hand.pop(0)
        player.hand.pop(0)
        player.hand.append(Change[answer])
        player.hand.append(Change[answer2])
        for i in Change:
            if i != Change[answer] and i != Change[answer2]:
                self.dealer.deck.append(i) 

    def challenge(self, player):
        answer = input(f"{player.name}, do you want to challenge him/her?: ")
        if answer == "y":
            return True     
        elif answer == "n":
            return False

    def yes_challenge(self, player):
        player.look_at_the_hand()

        for i in player.hand:
            if value == i.type:
                return True
            else:
                return False
    









    def turn(self,player):
        while True:
            print(f'\n{player.name} Turn!:')
            self.show_people()
            print('\nDead Cards:')
            self.dealer.print_dead_deck()
            select = self.console.print_turn_menu()
            if select == 0:
                player.look_at_the_hand()

            elif select == 1:
                select2 = self.console.print_general_action_menu()

                if select2==0:
                    self.hit(player)
                    #esta accion no puede ser bloqueada
                  
                elif select2==1:
                    self.income(player)

                elif select2==2:
                    self.foreign_aid(player)          
                break

            elif select==2:
                select2=self.console.print_character_action_menu()

                if select2==0:
                    player.duke_tax(player)
                    """
                    value = "Duke"
                    if yes_challenge(player) == True:
                        player.duke_tax(player)
                    else:
                        print("You don´t have the card, you loose ......")
                        pass
                    """
                elif select2==1:
                    
                    self.assassin(player)
                    
                elif select2==2:
                    self.captain_extortion(player)
                    
                elif select2==3:
                    self.ambassador_change(player)
                break



