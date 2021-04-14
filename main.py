from person import Person
from numpy import random
from random import shuffle

print("\n We must first start by creating the players.")
print("Remember that only can play 3-4 players")
people = []
money = []
cards_number = []
cards = ["Duke", "Assassin", "Captain", "Ambassador", "Countess", 
        "Duke", "Assassin", "Captain", "Ambassador", "Countess", 
        "Duke", "Assassin", "Captain", "Ambassador", "Countess"]
shuffle(cards)


def print_menu_and_select():
    print("Select an option: ")
    print("0. Start the game ")
    print("1. Add player ")
    print("2. Show players ")
    print("3. Show all the players information")
    return int(input())

def create_person():
    name = input("Enter players name: ")
    money = 2
    deck = []
    deck.append(cards[0])
    deck.append(cards[1])
    cards.pop(0)
    cards.pop(0)
    people.append(Person(name, money, deck))

def show_people():
    print("\nPeople created:")
    for (i, _) in enumerate(people):
        print(f"{i}: {people[i].name} ")

def show_peoples_info():
    print("\n player coins at the moment:")
    for (i, _) in enumerate(people):
        print(f"{i}: {people[i].name} has {people[i].money} coins and his deck is {people[i].deck} ")

def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            if 3 <= len(people) <= 4:
                break
            else:
                raise ValueError("Remember that you can only play with 3 or 4 players")
        if selection == 1:
            create_person()
        if selection == 2:
            show_people()
        if selection == 3:
            show_peoples_info()
         

if __name__== "__main__":
    menu()

