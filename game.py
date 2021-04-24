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

    def show_all_the_people_info(self):
        for i in self.player_list:
            for j in i.hand:
                print(j.type)


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
        self.you_lost(self.player_list[question])

    def assassin(self, player):
        player.plus_money(-3)
        print("Who do you want to Assassin?")
        for (i, _) in enumerate(self.player_list):
            if self.player_list[i] == player:
                continue
            else:
                print(f"{i}: {self.player_list[i].name}")
        question = int(input("(Select (0,1,2,3): "))
        print(f"\n The player {self.player_list[question].name} has to turn up a card")
        j = 0
        for i in self.player_list[question].hand:
            print(j,":", i.type)
            j += 1 
        answer = int(input("Select an option (0/1): "))
        self.dealer.dead_deck.append(self.player_list[question].hand[answer])
        self.player_list[question].hand.pop(answer)
        self.you_lost(self.player_list[question])


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
        answer = input(f"{player.name}, do you want to challenge him/her? (y/n): ")
        if answer == "y":
            return True     
        elif answer == "n":
            return False

    def yes_challenge(self, player,value):
        player.look_at_the_hand()
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
        answer = ""
        answer2 = ""
        answer3=''
        for i in self.player_list:
            if i != player:
                game_challenge = self.challenge_part1(i)
                if game_challenge == True:
                    v = self.yes_challenge(player,value)
                    if v == True:
                        print(f'\n{player.name}, you won the challenge')
                        answer = True
                        self.dealer.deck.append(card(value))
                        j = 0
                        for p in player.hand:
                            if p.type == value:
                                player.hand.pop(j)
                            j+=1
                        self.dealer.deal_card(player)
                        print(f'\n{i.name}, you lost the challenge, turn up a card!')
                        i.look_at_the_hand()
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(i.hand[answer])
                        i.hand.pop(answer)
                        self.you_lost(i)
                        answer3=1
                        break
                  
                    else:
                        print(f'\n {player.name} you lost the challenge, turn up a card:')
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(player.hand[answer])
                        player.hand.pop(answer)
                        self.you_lost(player)
                        answer = False
                        answer3=1
                        break
                elif game_challenge == False:
                    answer2 = True
        if answer == True:
            return True
        elif answer2 == True:
            return 0
        elif answer3 == 1:
            return 1
        else:
            return False
    
    def counterattack_part1(self, player):
            answer = input(f"{player.name}, do you want to counterattack him/her? (y/n): ")
            if answer == "y":
                return True     
            elif answer == "n":
                return False

    def counterattack(self, player, value):
        for i in self.player_list:
            if i != player:
                game_counterattack = self.counterattack_part1(i)
                if game_counterattack == True:
                    a = self.challenge(i, value)
                    if a == True:
                        return False
                
                    elif a == 0:
                        return True
                    else:
                        return True
                else:
                    continue

    def yes_challenge_with_2_values(self, player, value, value2):
            player.look_at_the_hand()
            if len(player.hand) == 2:
                if player.hand[0].type == value or player.hand[1].type == value or player.hand[0].type == value2 or player.hand[1].type == value2:
                    return True
                else:
                    return False
            elif len(player.hand) == 1:
                if player.hand[0].type == value or player.hand[0].type == value2:
                    return True
                else:
                    return False

    def challenge_with_2_values(self, player, value, value2):
        answer = ""
        answer2 = ""
        for i in self.player_list:
            if i != player:
                game_challenge = self.challenge_part1(i)
                if game_challenge == True:
                    v = self.yes_challenge_with_2_values(player,value, value2)
                    if v == True:
                        print(f'\n{player.name}, you won the challenge')
                        answer = True

                        #revisar aca
                        self.dealer.deck.append(card(value))
                        j = 0
                        for p in player.hand:
                            if p.type == value or p.type == value2:
                                player.hand.pop(j)
                            j+=1
                        self.dealer.deal_card(player)
                        print(f'\n{i.name}, you lost the challenge, turn up a card!')
                        i.look_at_the_hand()
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(i.hand[answer])
                        i.hand.pop(answer)
                        break
                    else:
                        print(f'\n {player.name} you lost the challenge, turn up a card:')
                        answer = int(input('Choose a card: '))
                        self.dealer.dead_deck.append(player.hand[answer])
                        player.hand.pop(answer)
                        answer = False
                        break
                elif game_challenge == False:
                    answer2 = True
        if answer == True:
            return True
        if answer2 == True:
            return 0
        else:
            return False

    def counterattack_with_2_values(self, player, value, value2):
          for i in self.player_list:
            if i != player:
                game_counterattack = self.counterattack_part1(i)
                if game_counterattack == True:
                    a = self.challenge_with_2_values(i, value, value2)
                    if a == True:
                        return False
                    elif a == 0:
                        return True
                    else:
                        return True
                else:
                    continue

    def you_lost(self, player):
        if len(player.hand) == 0:
            j = 0
            for i in self.player_list:
                if i.name == player.name: 
                    print(f"{player.name}, you lost") 
                    self.player_list.pop(j)
                j += 1

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

                if select2 == 0:
                    self.hit(player)
                    #esta accion no puede ser bloqueada
                    break
                elif select2 == 1:
                    self.income(player)
                    #esta accion no puede ser bloqueada
                    break
                elif select2 == 2:
                    x = self.counterattack(player, 'Duke')
                    if x == True:
                        self.foreign_aid(player)
                    break
            elif select == 2:
                select2 = self.console.print_character_action_menu()

                if select2 == 0:
                    y = self.challenge(player,'Duke')
                    if y == True or y == 0:
                        print("You earned 3 coins! ")
                        self.duke_tax(player)
                    break

                elif select2 == 1: 
                    y = self.challenge(player,'Assassin')
                    if y == 1:
                        break
                    elif y == True:
                        self.assassin(player)
                    elif y == 0:
                        c = self.counterattack(player, 'Contessa')
                        if c == False or c == True:
                            print("You avoided the murder succesfully")
                        else:
                            self.assassin(player)
                    else:
                        self.assassin(player) 
                    break  

                elif select2 == 2:
                    y = self.challenge(player,'Captain')
                    if y == True or y == 0:
                        x = self.counterattack_with_2_values(player, 'Ambassador', 'Captian')
                        #falta capitan
                        if x == False or y == 0:
                            print("You avoided the extortion successfully")
                        else:
                            self.captain_extortion(player)        
                    break    
                elif select2 == 3:
                    y = self.challenge(player,'Ambassador')
                    if y == True or y == 0:
                        self.ambassador_change(player)
                    break

                
               
            



