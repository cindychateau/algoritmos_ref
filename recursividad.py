#RECURSIVIDAD: Una función que se llama a sí misma
#1.- Caso base
#2.- Cómo va a avanzar mi función
#3.- Volver a llamar la función

#hola(cantidad) - Función que imprime N cantidad de veces la palabra Hola
#hola(4)
#cantidad = 4
#PRINT Hola
#hola(3)

#hola(3)
#cantidad = 3
#PRINT Hola
#hola(2)

#hola(2)
#cantidad = 2
#PRINT Hola
#hola(1)

#hola(1)
#cantidad = 1
#PRINT Hola
#hola(0)

#hola(0)
def hola(cantidad):
    if cantidad > 0:
        print("Hola")
        hola(cantidad - 1)

hola(4)

#RETO 1 - Función de cuenta regresiva que recibe un número e imprime todos los numeros desde el que recibe hasta el 0.
#Ej. 10 -> 10 9 8 7 6 5 4 3 2 1 0
def cuentaRegresiva(num):
    if num > -1:
        print(num)
        cuentaRegresiva(num -1)

cuentaRegresiva(10)

#SIGMA - Recibe un número y va sumando todos los números anteriores.
#RETO 2 - Función sigma, que reciba un número y regrese la sumatoria correspondiente a ese sigma.
#Ej. 5 = 5+4+3+2+1    8= 8+7+6+5+4+3+2+1 .    1=1
#sigma(5)
#num = 5
#RETURN 5 + sigma(4) * -> 5 + 10 -> 15

#sigma(4)
#num = 4
#RETURN 4 + sigma(3) * -> 4 + 6 -> 10

#sigma(3)
#num = 3
#RETURN 3 + sigma(2) * -> 3 + 3 -> 6

#sigma(2)
#num = 2
#RETURN 2 + sigma(1) * ->2 + 1 -> 3

#sigma(1)
#num = 1
#RETURN 1
def sigma(num):
    if num == 1:
        return 1
    else:
        return num + sigma(num - 1)

print(sigma(5))

#RETO GRUPAL: Función factorial recursiva. Función que reciba un número y regrese el número factorial.
#Ej. 4 -> 4*3*2*1


#RETO GRUPAL: Función fibonacci recursiva. Función que recibe un num positivo y regresa el número recibido de la serie de fibonacci
#Serie: 0 1 1 2 3 5 8 13 21 . 5