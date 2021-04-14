from dealer import dealer
from game import game
from player import Player
from random import shuffle


def print_menu_and_select():
    print("Select an option: ")
    print("0. Start the game ")
    print("1. Add player ")
    print("2. Show players ")
    print("3. Show all the players information")
    print('4. Quit')
    return int(input())



def menu():
    Game=game()
    Dealer=dealer()
    Dealer.deck_shuffle
    print("\n We must first start by creating the players.")
    print("Remember that only can play 3-4 players")
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            try:
                Game.start_game()
            except ValueError as e:
                print(e)
        if selection == 1:
            Game.create_person(Dealer)
            
        if selection == 2:
            Game.show_people()
        if selection == 3:
            show_peoples_info()
        if selection == 4:
            break
         

if __name__== "__main__":
    menu()

