from person import Person

print("\n We must first start by creating the players.")
people = []
money = []
cards = ["Duque", "Asesino", "Capitan", "Embajador", "Condesa", 
        "Duque", "Asesino", "Capitan", "Embajador", "Condesa", 
        "Duque", "Asesino", "Capitan", "Embajador", "Condesa"]

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

            break
        if selection == 1:
            create_person()
        if selection == 2:
            show_people()
        if selection == 3:
            show_peoples_money()



if __name__== "__main__":
    menu()
    