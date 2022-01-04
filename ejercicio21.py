#Realice una aplicacion en python que permita generar la tabla de multiplicar de un número ingresado 
#entrada
numero = int(input("Ingrese un número: "))
contador = 1
resultado = 0 
#proceso
while contador < 13:
    resultado = numero * contador
    contador = contador + 1 
    print(resultado)