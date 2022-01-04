#ejercicio10
s=0
i=0
n = int(input("Ingresa un número binario de 4 dígitos: "))
while n>=1:
    d=n%10
    n=n//10
    s=s+d*pow(2,i)
    i=i+1
print(s)
