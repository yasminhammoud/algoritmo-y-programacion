""" 
Los vendedores del samán electrónico tiene una política de cambio diferente a otras tiendas, ellos calculan el precio de un artículo en bolívares, multiplicando por la tasa de cambio promedio y luego le aumenta un 10% a ese nuevo valor, realice un programa que reciba el monto en dólares y la tasa de cambio e imprima en pantalla el valor del artículo.

Input:
Ingrese el monto en dólares: 20
Ingrese la tasa de cambio usd/ves: 150000

Output Esperado:
El monto en Bolivares es: 3300000.0000000005

"""
monto_dolares = float(input("Ingrese el monto en dólares: "))
tasa_cambio = float(input("Ingrese la tasa de cambio usd/ves: "))
monto_cambio = monto_dolares*tasa_cambio
monto_total = monto_cambio*1.1
print(f"El monto en Bolivares es: {monto_total}")