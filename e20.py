#ejercicio20
d=int(input("Ingrese dia: "))
m=int(input("Ingrese mes: "))
print("La fecha que usted eligió es: {}/{}/2014".format(d,m))
n=0
if m == 1:
    n=0
elif m == 2:
    n = 31
elif m == 3:
    n = 59
elif m == 4:
    n = 90
elif m == 5:
    n = 120
elif m == 6:
    n = 151
elif m == 7:
    n = 181
elif m == 8:
    n = 212
elif m == 9:
    n = 243
elif m == 10:
    n = 273
elif m == 11:
    n = 304
elif m == 12:
    n = 334   
else:
    print("Esa fecha no existe")
r=n+d
print("han pasado {} dias desde el 1 de enero del 2014".format(r))
