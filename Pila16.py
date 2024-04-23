# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. 
# Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, 
# es decir los personajes que aparecen en ambos episodios.

from Pila import Stack

episodioV = Stack()
episodioVII = Stack()

def cargar (pila, lista):
    for personaje in lista:
        pila.push(personaje)

personajesV = [
    "Luke Skywalker",
    "Han Solo",
    "Leia Organa",
    "Lando Calrissian",
    "Darth Vader",
    "C-3PO",
    "Yoda",
    "Obi-Wan Kenobi",
    "Boba Fett",
    "Chewbacca",
    "R2-D2",
    "Admiral Firmus Piett",
    "General Veers",
    "Admiral Ozzel",
    "Captain Needa"
]
cargar(episodioV, personajesV)

personajesVII = [
    "Rey",
    "Finn",
    "Poe Dameron",
    "Kylo Ren",
    "Leia Organa",
    "Han Solo",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "BB-8",
    "Luke Skywalker",
    "Supreme Leader Snoke",
    "General Hux",
    "Captain Phasma"
]
cargar(episodioVII, personajesVII)

for i in range (episodioV.size()):
    aux = Stack()
    for j in range (episodioVII.size()):
        personaje = episodioVII.on_top()
        if episodioV.on_top() == personaje:
            print(f"el personaje {personaje} aparece en ambos episodios")
        aux.push(episodioVII.pop())
    episodioVII = aux
    episodioV.pop()