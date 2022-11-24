#array = [5, 3, 2, 10, 4]
#j -> 0 - 4
#j = 0
#posicion_menor = 0
#i -> 1 - 4
#i = 1
#array[1] < array[0] -> 3 < 5
#posicion_menor = 1
#i = 2
#array[2] < array[1] -> 2 < 3
#posicion_menor = 2
#i = 3
#array[3] < array[2] -> 10 < 2
#i = 4
#array[4] < array[2] -> 4 < 2
#temp = array[2] = 2
#array[2] = array[0] = 5
#array[0] = 2
#array = [2, 3, 5, 10, 4]

#j = 1
#posicion_menor = 1
#i -> 2 - 4
#i = 2
#array[2] < array[1] -> 5 < 3
#i = 3
#array[3] < array[1] -> 10 < 3
#i = 4
#array[4] < array[1] -> 4 < 3
#array = [2, 3, 5, 10, 4]

#j = 2
#posicion_menor = 2
#i = 3 - 4
#i = 3
#array[3] < array[2] -> 10 < 5
#i = 4
#array[4] < array[2] -> 4 < 5
#posicion_menor = 4
#temp = array[4] = 4
#array[4] = array[2] = 5
#array[2] = 4
#array = [2, 3, 4, 10, 5]

#j = 3
#posicion_menor = 3
#i -> 4 - 4
#i = 4
#array[4] < array[3] -> 5 < 10
#posicion_menor = 4
#temp = array[4] = 5
#array[4] = array[3] = 10
#array[3] = 5
#array = [2, 3, 4, 5, 10]
def selectionSort(array):
    #Primer for corresponde a la posición que yo quiero comparar/reemplazar
    for j in range(len(array)):
        posicion_menor = j
        #Segundo for representa la comparación
        for i in range(j+1, len(array)):
            #Si de mi arreglo el valor que tengo en posicion i es menor a lo que tengo en posicion menor
            if array[i] < array[posicion_menor]:
                posicion_menor = i
        
        #Hacemos switch entre posicion_menor y j
        temp = array[posicion_menor]
        array[posicion_menor] = array[j]
        array[j] = temp