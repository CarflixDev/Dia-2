#Segundo programa del dia 2
#CarReel
#Fecha : 26/02/2024

nombre = input("¿Cual es su nombre? :")
ventas = int(input("Cual ha sido la venta de este mes? : "))
comisiones = round(ventas * 13/100,2)

print(f"El vendedor {nombre} este mes ha vendido {ventas}€ y ha obtenido una comision de {comisiones}€")