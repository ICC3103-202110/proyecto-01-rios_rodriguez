from card import card
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
        question = int(input("Select (0,1,2): "))
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

    def challenge_part1(self, player):
        answer = input(f"{player.name}, do you want to challenge him/her?: ")
        if answer == "y":
            return True     
        elif answer == "n":
            return False

    def yes_challenge(self, player,value):
        player.look_at_the_hand()
        lista=[]
        if len(player.hand) == 2:
            if player.hand[0].type == value or player.hand[1].type == value:
                return True
            else:
                return False
        elif len(player.hand) == 1:
            if player.hand[0].type == value:
                return True
            else:
                return False


    def challenge(self,player,value):
        for i in self.player_list:
            if i != player:
                game_challenge = self.challenge_part1(i)
                if game_challenge == True:
                    v = self.yes_challenge(player,value)
                    if v == True:
                        print('You won the challenge')
                        answer = True
                        self.dealer.deck.append(card(value))
                        j = 0
                        for p in player.hand:
                            if p.type == value:
                                player.hand.pop(j)
                            j+=1
                        self.dealer.deal_card(player)
                        print('You lose, turn up a card!')
                        i.look_at_the_hand()
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(i.hand[answer])
                        i.hand.pop(answer)
                        break

                    else:
                        print('You lose, turn up a card:')
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(player.hand[answer])
                        player.hand.pop(answer)
                        answer = False
                        break
                elif game_challenge == False:
                    answer = True
        if answer == True:
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

            elif select == 2:
                select2 = self.console.print_character_action_menu()

                if select2 == 0:
                    for i in self.player_list:
                        if i != player:
                            game_challenge = self.challenge_part1(i)
                            if game_challenge == True:
                                value = "Duke"
                                v = self.yes_challenge(player,value)
                                if v == True:
                                    print(f'{player.name} you won the challenge')
                                    answer = True
                                    self.dealer.deck.append(card(value))
                                    j = 0
                                    for p in player.hand:
                                        if p.type == value:
                                            player.hand.pop(j)
                                        j+=1
                                    self.dealer.deal_card(player)
                                    print(f'{i.name} you lose, turn up a card!')
                                    i.look_at_the_hand()
                                    answer = int(input('Choose a card: '))
                                    self.dealer.dead_deck.append(i.hand[answer])
                                    i.hand.pop(answer)
                                    break

                                else:
                                    print(f'{player.name} you lose, turn up a card:')
                                    answer = int(input('Choose a card: '))
                                    self.dealer.dead_deck.append(player.hand[answer])
                                    player.hand.pop(answer)
                                    answer = False
                                    break
                            elif game_challenge == False:
                                answer = True
                    if answer == True:
                        self.duke_tax(player)

                    else:
                        pass
                 
                elif select2==1:
                
                    y=self.challenge(player,'Assassin')
                    if y == True:
                        self.assassin(player)

                    
                elif select2==2:
                    y=self.challenge(player,'Captain')
                    if y == True:
                        self.captain_extortion(player)
                    
                elif select2==3:
                    y=self.challenge(player,'Ambassador')
                    if y == True:
                        self.ambassador_change(player)
                break



