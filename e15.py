#ejercicio5
s=int(input("Ingrese los segundos que desee convertir: "))





if s>=60:
    m= s/60
    print("\n en MINUTOS: {} minuto(s)".format(m))
else:
    print("\n en MINUTOS: 0 minuto(s)")

if s>=3600:
    h= s/3600
    print("\n en HORAS: {} hora(s)".format(h))
else:
    print("\n en HORAS: 0 dia(s)")

if s>=86400:
    d= s/86400
    print("\n en DIAS: {} dia(s)".format(d))
else:
    print("\n en DIAS: 0 dia(s)")


