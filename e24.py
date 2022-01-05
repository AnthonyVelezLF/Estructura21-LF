#ejercicio24
n = int(input("Ingresa un número entero: "))

s = str(n)
reverso = s[::-1]

if s == reverso:
    print("SI es capicúa")
else:
    print("NO es capicúa") 