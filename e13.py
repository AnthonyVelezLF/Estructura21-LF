#ejercicio13
n = int(input("Ingresa un número de 5 dígitos: "))

s = str(n)
reverso = s[::-1]

if s == reverso:
    print("SI es capicúa")
else:
    print("NO es capicúa") 
