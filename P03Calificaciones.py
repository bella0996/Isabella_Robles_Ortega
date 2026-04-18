# Pedir las calificaciones
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio
promedio = (cal1 + cal2 + cal3) / 3

# Mostrar el resultado
print("Tu promedio es:", promedio)

# Evaluar con if-else
if promedio >= 6:
    print("Aprobaste")
else:
    print("Reprobaste")