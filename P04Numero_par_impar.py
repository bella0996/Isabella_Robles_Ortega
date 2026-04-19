#Isabella Nahomy Robles Ortega
num = int(input("Ingresa un número: "))

if (num % 2 == 0 and not num % 2 != 0):
    print("El número es par")
elif (num % 2 != 0 or not num % 2 == 0):
    print("El número es impar")
else:
    print("Error")
