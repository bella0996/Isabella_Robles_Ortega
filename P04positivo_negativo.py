# Pedir el número
num = float(input("Ingresa un número: "))

# Evaluar el número
if num > 0 and not num == 0:
    print("El número es positivo")
elif num < 0 or not num > 0:
    print("El número es negativo")
else:
    print("El número es cero")