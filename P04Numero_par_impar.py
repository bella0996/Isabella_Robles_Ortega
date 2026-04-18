# Pedir el número
num = int(input("Ingresa un número: "))

# Evaluar si es par o impar
if (num % 2 == 0 and not num % 2 != 0):
    print("El número es par")
elif (num % 2 != 0 or not num % 2 == 0):
    print("El número es impar")
else:
    print("Error")