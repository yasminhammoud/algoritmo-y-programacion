"""
Construye un programa, que al recibir como datos el costo de un artículo vendido y 
la cantidad de dinero entregada por el cliente, calcule e imprima el cambio que se 
debe entregar al cliente, asume que usuario siempre ingresara los datos correctos.

    Entradas: Costo: 12, Dinero: 15
    Salida: "El cambio del cliente es: 3.0"
      
    Entradas: Costo: 12, Dinero: 12
    Salida: "El cliente no tiene cambio"

    Entradas: Costo: 15, Dinero: 10
    Salida: "El cliente debe dinero"
"""

costo = float(input("Costo de artículo vendido: "))
entrada = float(input("Cantidad de dinero entregada por el cliente: "))
if costo==entrada:
    print("El cliente no tiene cambio")
elif costo<entrada:
    cambio = entrada-costo
    print(f"El cambio del cliente es: {cambio}") 
elif costo>entrada:
    print("El cliente debe dinero")