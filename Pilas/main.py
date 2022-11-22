from Nodo import Nodo
from Pila import Pila

nodo1 = Nodo("N1")
nodo2 = Nodo("N2")
nodo3 = Nodo("N3")

pila = Pila() #Inicia vacía

pila.push(nodo1) #Top: N1
pila.push(nodo3) #Top: N3, N1
pila.push(nodo2) #Top: N2, N3, N1

pila.imprime()