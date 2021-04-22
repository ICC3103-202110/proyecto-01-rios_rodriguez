from dealer import dealer
from console import Console
from game import game
from player import Player
from random import shuffle

def menu():
    Game=game()
    Game.dealer.deck_shuffle
    print("\nWe must first start by creating the players.")
    print("Remember that only can play 3 or 4 players")
    while True:
        selection = Game.console.print_menu_and_select()
        if selection == 0:
            try:
                var=Game.start_game()
                while var:
                    for a in Game.player_list:
                        Game.turn(a)
                        
                        for j in Game.player_list:
                            if j!=a:
                                game_challenge = Game.challenge(j)
                                if game_challenge == True:
                                    Game.yes_challenge(a)
                                    pass
                                else:
                                    pass
    
                    break
            except ValueError as e:
                print(e)
        if selection == 1:
            Game.create_person()
            
        if selection == 2:
            Game.show_people()
        if selection == 3:
            break
         
if __name__== "__main__":
    menu()





