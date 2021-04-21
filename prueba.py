from player import Player
from dealer import dealer
from card import card
from game import game

Game=game()
contador = 0 
while True:
    
    print(f"Starts {Game.player_list[contador]}. He/she has {Game.player_list[contador].hand}")
    answer = input("What action do you want to do? ")
    
    if answer == "hit":
        hit()
    elif answer == "income":
        income()
    elif answer == "foreign aid":
        challenge()
        # buscar la manera de que si alguien lo desafia, no entre a esta funcion
        counterattack()
        foreign_aid()

    elif answer == "duke tax":
        challenge()
        duke_tax()

    elif answer == "assassin murder":
        challenge()
        counterattack()
        assassin_murder()

    elif answer == "captain extortion":
        challenge()
        counterattack()
        captain_extortion()

    elif answer == "ambassador change":
        challenge()
        counterattack()
        ambassador_change()

    contador += 1
    question = int(input("0. Quit "))
    if question == 0:
        break


def challenge():
    print("Someone wants to challenge him/her? (Yes/No)")
    for (i,_) in enumerate(self.player_list)):
        answer = input(f"{self.player_list[i].name}: ")
        # ver el tema de que no se caiga si uno pone yes or no en minuscula
        if answer == "Yes":
            continue
        elif answer == "No":
            continue
    
def counterattack():

    if answer == "assassin murder":
        print("Show that you have the card to stop the murderer")
        contessa_stop_murder()

    elif answer == "captain extortion":
        print("Show that you have the card to stop the extortion")
        ambassador_or_captain_stop_extortion()

    elif answer == "duke stop foreign aid":
        print("Show that you have the card to stop")
        duke_stop_foreign_aid()


def hit():
    print("This action costs 7 coins.")
    self.player_list[contador].money - 7
    input("Who do you want to hit? ")
    #hay que poder seleccionar al jugador elegido para que se aplique en la funcion turn card

    turn_card()


def turn_card():
    print(f"{self.player_list[i]}, what card do you want to turn?")
    print(f"options: ")
    pass

def income():
    return self.player_list[contador].money + 1

def foreign_aid():
    return self.player_list[contador].money + 2

def duke_tax():
    return self.player[contador].money + 3

def assassin_murder():
    pass

def captain_extortion():
    pass

def ambassador_change():
    pass

def duke_stop_foreign_aid():
    pass

def contessa_stop_murder():
    pass

def ambassador_or_captain_stop_extortion():
    pass



game1()

if answer == "hit":
    hit()
elif answer == "income":
    income()
elif answer == "foreign aid":
    challenge()
    # buscar la manera de que si alguien lo desafia, no entre a esta funcion
    counterattack()
    foreign_aid()

elif answer == "duke tax":
    challenge()
    duke_tax()

elif answer == "assassin murder":
    challenge()
    counterattack()
    assassin_murder()

elif answer == "captain extortion":
    challenge()
    counterattack()
    captain_extortion()

elif answer == "ambassador change":
    challenge()
    counterattack()
    ambassador_change()





