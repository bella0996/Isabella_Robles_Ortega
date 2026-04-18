# Pedir datos
edad = int(input("Ingresa tu edad: "))
tiene_boleto = input("¿Tienes boleto? (si/no): ").lower()
esta_en_lista = input("¿Estás en la lista VIP? (si/no): ").lower()

# Evaluar acceso
# Puede entrar si:
# - Tiene 18 o más Y tiene boleto
# - O está en lista VIP
# - Pero NO entra si es menor de 16
if ((edad >= 18 and tiene_boleto == "si") or esta_en_lista == "si") and not edad < 16:
    print("Acceso permitido")
else:
    print("Acceso denegado")