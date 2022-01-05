#ejercicio22
m=int(input("Ingrese el monto a pagar: "))
if m > 1000:
    print("\ntiene un descuento del 20%")
    m=m*0.80
    print("El monto a pagar ahora es: {}".format(m))
else:
    print("\nNo tiene ningún descuento")
    print("El monto a pagar es: {}".format(m))
    