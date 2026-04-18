# Pedir datos
precio = float(input("Ingresa el precio del producto: "))
es_estudiante = input("¿Eres estudiante? (si/no): ").lower()
compra_mayor = input("¿Tu compra es mayor a 1000? (si/no): ").lower()

# Aplicar descuento
# Descuento si es estudiante Y la compra es mayor a 1000
# O si NO es estudiante pero la compra es mayor a 2000
if (es_estudiante == "si" and compra_mayor == "si") or (not es_estudiante == "si" and precio > 2000):
    descuento = precio * 0.20
    total = precio - descuento
    print("Se aplicó un 20% de descuento")
else:
    total = precio
    print("No aplica descuento")

# Mostrar total
print("Total a pagar:", total)