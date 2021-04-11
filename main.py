from person import Person

print("\n We must first start by creating the players.")
people = []

def print_menu_and_select():
    print("Select an option: ")
    print("0. Start the game ")
    print("1. Add player ")
    print("2. Show players ")
    return int(input())

def create_person():
    name = input("Enter player name: ")
    rut = input('Enter player id:')
    people.append(Person(rut,name))

def show_people():
    l1 = list(range(0, len(people)))
    for i in l1:
        print(people[i].name)

def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            create_person()
        if selection == 2:
            show_people()


if __name__== "__main__":
    menu()