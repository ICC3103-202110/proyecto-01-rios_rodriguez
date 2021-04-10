class Person:
    def _init_(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

print("\n Primero debemos comenzar creando a los jugadores.")
people = []

def print_menu_and_select():
    print("Seleccione una de las siguientes opciones: ")
    print("0. Dejar de agregar jugadores y comenzar con el juego ")
    print("1. Agregar jugador ")
    print("2. Mostrar a los jugadores creados ")
    return int(input())

def create_person():
    name = input("Ingrese el nombre del jugador ")
    people.append(Person(name))

def show_people():
    l1 = list(range(0, len(people)))
    for i in l1:
        print(people[i].name)