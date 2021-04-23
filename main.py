from dealer import dealer
from console import Console
from game import game
from player import Player
from random import shuffle

def menu():
    Game = game()
    Game.dealer.deck_shuffle
    print("\nWe must first start by creating the players.")
    print("Remember that only can play 3 or 4 players")
    while True:
        selection = Game.console.print_menu_and_select()
        if selection == 0:
            try:
                var = Game.start_game()
                while var:
                    for a in Game.player_list:
                        Game.turn(a)
            except ValueError as e:
                print(e)
        if selection == 1:
            Game.create_person()
            
        if selection == 2:
            Game.show_people()
        if selection == 3:
            break
        if selection == 4:
            Game.show_all_the_people_info()
         
if __name__== "__main__":
    menu()





