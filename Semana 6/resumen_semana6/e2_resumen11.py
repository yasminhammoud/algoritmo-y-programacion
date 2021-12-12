
def datos(clientes):
    nombre = input("Nombre del cliente: ")
    while not ("".join(nombre.split(" "))).isalpha():
        nombre = input("Dato inválido, ingrese el nombre del cliente nuevamente: ")
    while True:
        try: 
            cedula = int(input("Cédula de indentidad del cliente: "))
        except ValueError as identifier:
            print("Ingreso inválido, intente de nuevo")
        try: 
            pago = int(input("Monto a cancerlar por el cliente: "))
        except ValueError as identifier:
            print("Ingreso inválido, intente de nuevo")
    
    cliente = {}
    cliente["Nombre"] = nombre
    cliente["Monto"] = pago
    clientes[cedula] = cliente

    return clientes

def numero_compras(cedula, clientes, cliente):
    compra_cliente = 0
    for cedula in clientes:
        compra_cliente +=1 
    cliente["Compras"]= compra_cliente

def descuento_oblongo(clientes):
    for cedula in clientes:
        cedula_list = [int(x.strip()) for x in cedula.split(',') if x]
        last_sum = cedula_list[-1] + cedula_list[-2] + cedula_list[-3]
        for n in last_sum:
            f = 0
            for i in range(n):
                if i * (i + 1) == x:
                    f = 1
                    break
                if f==1:
                    return 7%


def main():
    clientes = {}
    datos(clientes)

    main()