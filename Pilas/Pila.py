from Nodo import Nodo

class Pila:
    def __init__(self):
        self.top = None #Cuando inicializamos la pila está vacía
    

    #push - Ingresar un nuevo nodo a la pila
    #pila -> top: None
    #nuevoNodo = N3 nxt: None
    #N3.next = None
    #top = N3

    #pila = top: N3, ≠
    #pila.push(N2)
    #nuevoNodo = N2 next: None
    #N2.next = N3
    #top = N2

    #pila = top: N2, N3, ≠
    #pila.push(N1)
    #nuevoNodo = N1 next: None
    #N1.next = N2
    #top = N1
    #pila = top: N1, N2, N3, ≠

    def push(self, nuevoNodo):
        nuevoNodo.next = self.top
        self.top = nuevoNodo


    #imprime - Imprimir en orden todos los nodos
    def imprime(self):
        nodoActual = self.top
        while nodoActual != None:
            print(nodoActual.valor)
            nodoActual = nodoActual.next


    #pop - Eliminar el elemento que tengo en top de mi pila
    #pila = top: N2, N3, N1, ≠
    #pila.pop()
    #nodoActual = N2
    #top = N3
    #N2.next = None
    #pila = N3, N1, ≠
    def pop(self):
        nodoActual = self.top
        if nodoActual != None:
            self.top = nodoActual.next
            nodoActual.next = None #Reset, reestableciendo a los valores originales