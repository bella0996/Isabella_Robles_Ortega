#Isabella Nahomy Robles Ortega
# Tabla de multiplicar de un número
num = int(input("Ingresa un número: "))

for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
