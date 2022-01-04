#aplicacion que permita verificar si un numero esta dentro de un rango
#entrada
rangominimo = 1
rangomaximo = 5
numero = int(input("ingrese un numero pra evaluar si está en el rango: "))
#proceso
if numero>=rangominimo and numero<=  rangomaximo:
    print("El número está dentro de los rangos")
else:
    print("El número está fuera de los rangos")