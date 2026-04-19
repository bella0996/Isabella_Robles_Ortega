#Isabella Nahomy Robles Ortega
edad = int(input("Ingresa tu edad: "))
tiene_id = input("¿Tienes identificación oficial? (si/no): ").lower()

# Condiciones
# Mayor de edad si tiene 18 o más Y tiene identificación
# O si tiene más de 21 (aunque no tenga ID)
if (edad >= 18 and tiene_id == "si") or (edad > 21 and not tiene_id == "si"):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
