#FACTORIAL
#Recibimos un número y regresamos el factorial de este
#1! = 1*1 = 1
#2! = 1*2 = 2
#3! = 1*2*3 = 6
#4! = 1*2*3*4 = 24
#n = 3
#numFactorial = 1
#1 - n+1 -> range(1,4) -> 1, 2, 3
#i = 1
#numFactorial = 1*1 = 1
#i = 2
#numFactorial = 1*2 = 2
#i = 3
#numFactorial = 2*3 = 6
#RETURN 6
def factorial(n):
    numFactorial = 1
    for i in range(1, n+1):
        numFactorial *= i
    return numFactorial

#print(factorial(3))



#FIBONACCI
#Recibimos un número entero e imprimimos la serie de fibonacci en esa posición
#Serie Fibonacci: Comenzando en 0 y 1 vamos sumando los dos últimos números
#0 1 1 2 3 5 8 13 21 34 55 89
#n = 4
#listaFibonacci = [0, 1]
# 2 - 4 -> 2, 3
#i = 2
#siguienteNumero = listaFibonacci[2-1] + listaFibonacci[2-2] = 1 + 0 = 1
#listaFibonacci = [0, 1, 1]
#i = 3
#siguienteNumero = listaFibonacci[3-1] + listaFibonacci[3-2] = 1 + 1 = 2
#listaFibonacci = [0, 1, 1, 2]
def fibonacci(n):
    listaFibonacci = [0, 1]
    
    for i in range(2, n):
        siguienteNumero = listaFibonacci[i-1] + listaFibonacci[i-2]
        listaFibonacci.append(siguienteNumero)
    print(listaFibonacci)

#fibonacci(4)

#PALINDROMO
#Recibimos una palabra y nos regresa True o False si la palabra es palíndoma
#Ejemplo: oso, salas, seres, radar
#palabra = "alla"
#inicio = 0
#final = 3
#palabra[0] != palabra[3] -> a != a
#inicio = 1
#final = 2
#palabra[1] != palabra[2] -> l != l
#inicio = 2
#final = 1
def palindromo(palabra):
    inicio = 0
    final = len(palabra)-1 #la última posición de mi palabra

    while inicio < len(palabra) / 2:
        if palabra[inicio] != palabra[final]:
            return False
        else:
            inicio += 1
            final -= 1
    
    return True

print(palindromo("alla"))