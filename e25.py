#ejercicio25
numero = int(input("Ingrese un valor a evaluar: "))
cont=0
for n in range(1, numero+1):
    if numero % n == 0:
        cont += 1
if cont == 2:
  print("El numero ingresado si es primo")
else:
  print("El numero ingresado no es primo")