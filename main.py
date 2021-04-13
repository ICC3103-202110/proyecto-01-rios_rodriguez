from person import Person
from numpy import random
from random import shuffle

print("\n We must first start by creating the players.")
print("Remember that only can play 3-4 players")
people = []
money = []
cards_number = []
cards = ["Duque", "Assassin", "Capitan", "Embajador", "Condesa", 
        "Duque", "Assassin", "Capitan", "Embajador", "Condesa", 
        "Duque", "Assassin", "Capitan", "Embajador", "Condesa"]

def random_cards():
    shuffle(cards)
    print(cards)

def print_menu_and_select():
    print("Select an option: ")
    print("0. Start the game ")
    print("1. Add player ")
    print("2. Show players ")
    print("3. Show players money")
    print("4. None")
    return int(input())

def create_person():
    name = input("Enter players name: ")
    money = 2
    people.append(Person(name, money))

def show_people():
    print("\nPeople created:")
    for (i, _) in enumerate(people):
        print(f"{i}: {people[i].name} ")


def show_peoples_money():
    print("\n player coins at the moment:")
    for (i, _) in enumerate(people):
        print(f"{i}: {people[i].name} has {people[i].money} coins ")

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
            show_peoples_money()
        if selection == 4:
            random_cards()

if __name__== "__main__":
    menu()