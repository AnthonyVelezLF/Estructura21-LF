#ejercicio11
x = int(input("Ingresa un número de 4 dígitos: "))

u = x % 10
print("\nUnidades: ", u)

y = x - u 
y = y % 100
d = y // 10 
print("\nDecenas: ", d)

y = x - d*10 - u
y = y % 1000
c = y//100
print("\nCentenas: ", c)

y = x - c*100 - d*10 - u
um = y//1000
print("\nUnidades de Mil: {} \n".format(um))