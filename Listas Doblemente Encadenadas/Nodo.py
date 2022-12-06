class Nodo:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.next = None #El next se refiere al siguiente en la lista. Como aún mi nodo NO pertenece a ninguna lista, entonces su siguiente es NONE
        self.back = None #El back se refiere al anterior en la lista. Como aún mi nodo NO pertenece a ninguna lista, entonces su anterior es NONE