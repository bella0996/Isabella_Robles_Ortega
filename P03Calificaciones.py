#Isabella Nahomy Robles Ortega
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3

print("Tu promedio es:", promedio)

if promedio >= 6:
    print("Aprobaste")
else:
    print("Reprobaste")
