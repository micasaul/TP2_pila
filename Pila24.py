# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como 
# posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, 
# además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from Pila import Stack

mcu = Stack()

class personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

def cargar (pila, lista):
    for personaje in lista:
        pila.push(personaje)

personajes = [
    personaje("Iron Man", 8),
    personaje("Captain America", 7),
    personaje("Thor", 8),
    personaje("Black Widow", 8),
    personaje("Hulk", 6),
    personaje("Spider Man", 6),
    personaje("Nick Fury", 11),
    personaje("Hawkeye", 6),
    personaje("War Machine", 6),
    personaje("Loki", 6),
    personaje("Scarlet Witch", 5),
    personaje("Vision", 4),
    personaje("Black Panther", 5),
    personaje("Ant Man", 6),
    personaje("Star Lord", 6),
    personaje("Doctor Strange", 4),
    personaje("Groot", 6),
    personaje("Rocket", 6),
    personaje("Falcon", 5),
    personaje("Winter Soldier", 5),
    personaje("Captain Marvel", 4)
]

def RocketGroot (pila):
    aux = Stack()
    C_rocket=1
    C_groot=1
    for i in range (pila.size()):
        personaje=pila.pop()
        if personaje.nombre == "Rocket":
            print(f"Rocket se encuentra en la posicion {C_rocket} de la pila")
        if personaje.nombre == "Groot":
            print(f"Groot se encuentra en la posicion {C_groot} de la pila")
        C_rocket +=1
        C_groot +=1
        aux.push(personaje)
    return aux

def Mas5 (pila):
    aux=Stack()
    for i in range (pila.size()):
        personaje = pila.pop()
        if personaje.peliculas > 5:
            print(f"el personaje {personaje.nombre} aparece en {personaje.peliculas} peliculas")
        aux.push(personaje)
    return aux

def BlackWidow (pila):
    aux= Stack()
    for i in range(pila.size()):
        personaje = pila.pop()
        if personaje.nombre == "Black Widow":
            print(f"Black Widow participo en {personaje.peliculas} peliculas")
        aux.push(personaje)
    return aux

def Nombre (pila):
    aux=Stack()
    letras = ["C", "D", "G"]
    print("Los personajes cuyos nombres empiezan con C, D o G son: ")
    for i in range (pila.size()):
        personaje = pila.pop()
        if personaje.nombre[0] in letras:
            print(personaje.nombre)
        aux.push(personaje)
    return aux

cargar(mcu, personajes)
mcu = RocketGroot(mcu)
print()
mcu = Mas5(mcu)
print()
mcu = BlackWidow(mcu)
print()
mcu = Nombre(mcu)