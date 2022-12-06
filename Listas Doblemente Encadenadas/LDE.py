from Nodo import Nodo
class LDE:
    def __init__(self):
        self.head = None #Lo único que necesitamos es saber cuál es el primer nodo de mi lista. Cuando inicializamos nuestra lista aún NO tiene nodos, por lo tanto mi head es NONE

    def insertaNodo(self, nuevoNodo):
        #1.- Si mi head es vacía, entonces en nuevoNodo es el primero de la lista
        if self.head == None:
            self.head = nuevoNodo
        else:
            #2.- Recorro mi lista hasta que encuentre el último elemento de mi lista. Cómo sé cuál es? Es aquel que tiene como next None
            nodoActual = self.head #aux es el nodo en el que me encuentro en este momento
            while nodoActual.next != None:
                nodoActual = nodoActual.next
            nodoActual.next = nuevoNodo
            nuevoNodo.back = nodoActual

    def imprimeLista(self):
        nodoActual = self.head #Comenzamos con el primer elemento
        while nodoActual != None:
            print(nodoActual.nombre)
            nodoActual = nodoActual.next

    def eliminaNodo(self, id):
        nodoActual = self.head
        while(nodoActual != None):
            if nodoActual.id == id:
                nodoAnterior = nodoActual.back
                nodoSiguiente = nodoActual.next
                nodoAnterior.next = nodoSiguiente
                nodoSiguiente.back = nodoAnterior

                nodoActual.next = None
                nodoActual.back = None
            nodoActual = nodoActual.next

    