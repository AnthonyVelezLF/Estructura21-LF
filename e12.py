#ejercicio12
print("Ingrese una fecha en dd mm aaaa (separados con espacio): ", end=" ")
d, m, a = map(int, input().split())
print("\nla fecha que pusiste es: {}/{}/{}".format(d,m,a))

if a % 400 == 0:
    print("el año {} SI es bisiesto".format(a))
elif a %100 == 0:
    print("el año {} NO es bisiesto".format(a))
elif a %4 == 0:
    print("el año {} SI es bisiesto".format(a))
else:
    print("el año {} NO es bisiesto".format(a))
    

