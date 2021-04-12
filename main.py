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
    print("3. None")
    return int(input())

def create_person():
    name = input("Enter player name: ")
    person_id = int(input("ingrese su ID"))
    people.append(Person(name, person_id))

def show_people():
    l1 = list(range(0, len(people)))
    for i in l1:
        print(people[i].person_id)
    
def show_peoples_money():
    l1 = list(range(0, len(people)))
    for i in l1:
        print(f"{people[i].name} has {money} coins")

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
    