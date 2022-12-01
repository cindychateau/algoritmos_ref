from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None #Lo único que necesitamos es saber cuál es el primer nodo de mi lista. Cuando inicializamos nuestra lista aún NO tiene nodos, por lo tanto mi head es NONE

    #Función que mi ingresa un nuevo nodo la lista
    #HEAD: ≠
    #nuevoNodo = Elena next: ≠
    #HEAD: Elena next: ≠

    #nuevoNodo = Juana next: ≠
    #nodoActual = Elena
    #Elena.next = Juana
    #LE -> HEAD: Elena next: Juana, Juana next: ≠

    #nuevoNodo = Pablo next: ≠
    #nodoActual = Elena
    #nodoActual = Juana
    #Juana.next = Pablo
    #LE -> HEAD: Elena next: Juana, Juana next: Pablo, Pablo next: ≠
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

    #Función que me imprima la lista que yo tengo
    #LE -> HEAD: Elena next: Juana, Juana next: Pablo, Pablo next: ≠
    #nodoActual = Elena
    #PRINT Elena
    #nodoActual = Juana
    #PRINT Juana
    #nodoActual = Pablo
    #PRINT Pablo
    #nodoActual = ≠
    def imprimeLista(self):
        nodoActual = self.head #Comenzamos con el primer elemento
        while nodoActual != None:
            print(nodoActual.nombre)
            nodoActual = nodoActual.next
    
    #Función que elimine un nodo en base a su id
    #LE -> HEAD: 1 Elena next: Juana, 3 Juana next: Pablo, 5 Pablo next: ≠
    #id = 3
    #nodoActual = Elena
    #nodoPrevio = Elena
    #nodoActual = Juana
    #Elena.next = Juana.next = Pablo
    #Juana.next = ≠
    def eliminaNodo(self, id):
        if self.head == None: #Si el head es none, mi lista está vacía
            print("Lista vacía, no podemos eliminar nodos")
        else:
            nodoActual = self.head
            if nodoActual.id == id:
                #1.- El nuevo head debe ser el next de mi nodo actual
                self.head = nodoActual.next
                #2.- El nodo que quiero eliminar, ahora el NEXT es None, porque ya no lo queremos ligar a ninguna lista
                nodoActual.next = None
            else:
                nodoPrevio = nodoActual
                while nodoActual.next != None:
                    nodoPrevio = nodoActual
                    nodoActual = nodoActual.next
                    #1.- Buscar en el nodo actual si hay una coincidencia en el ID
                    if nodoActual.id == id:
                        #2.- Un nodo antes del actual, quiero que su siguiente nodo sea el nodo siguiente del actual
                        nodoPrevio.next = nodoActual.next
                        #3.- Al nodo actual (el que voy a eliminar), le pongo como siguiente NONE
                        nodoActual.next = None

    