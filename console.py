class Console():
    
    def print_menu_and_select(self):
        print("Select an option: ")
        print("0. Start the game ")
        print("1. Add player ")
        print("2. Show players ")
        print('3. Quit')
        return int(input())

    def print_turn_menu(self):
         print("Select an option: ")
         print("0. Look at your hand ")
         print("1. General action ")
         print("2. Card action ")
         return int(input())

    def print_general_action_menu(self):
         print("Select an option: ")
         print("0. Coup (hit) ")
         print("1. Income ")
         print("2. Foreign aid ")
         return int(input())

    def print_character_action_menu(self):
         print("Select an option: ")
         print("0. Duke tax ")
         print("1. Assassin Murder ")
         print("2. Captain Extortion ")
         print("3. Ambassador Change")
         return int(input())