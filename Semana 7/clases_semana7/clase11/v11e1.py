from Client import Client 

def register_client():
    while True: 
        try: 
            name = input("Nombre completo: ")
            dni = input("Dni: ")
            birthdate = input("Fecha de nacimiento: ")
            gender = input("Sexo: (M)Masculino (F)Femenino ").upper()
            balance = float(input("Balance: "))
            if balance < 100:
                print("El deposito minimo deber ser 100 USD")
                raise Exception
            break 
        
        except: 
            print("Error, valide sus datos")
    
    client = Client(name, dni, birthdate, gender, balance)
    print("\nRegistrado exitosamente!")
    return client

def check_balance(clients):
    dni = input('Ingrese su DNI: ')
    for client in clients:
        if client.dni == dni:
            client.my_balance()
            return True
    return False 

def deposit(clients):
    dni = input('Ingrese su DNI: ')
    for client in clients:
        if client.dni == dni:
            while True: 
                try:
                    amount = float(input('Ingrese monto: '))
                    if amount < 0:
                        print('El monto debe ser positivo')
                        raise Exception 
                    break 
                except:
                    print('Error, valide sus datos') 
            client.deposit(amount)
            print('Deposito realizado con éxito')
            return True
    return False 

def withdraw(clients):
    dni = input('Ingrese su DNI: ')
    for client in clients:
        if client.dni == dni:
            while True: 
                try:
                    amount = float(input('Ingrese monto: '))
                    if amount < 0:
                        print('El monto debe ser positivo')
                        raise Exception 
                    break 
                except:
                    print('Error, valide sus datos') 
            client.withdraw(amount)
            print('Retiro realizado con éxito')
            return True
    return False 

def main():
    clients = []
    while True:
        opcion = input(''' Bienvenido a Avila Bank 
        1.Registrar
        2. Ver Balance 
        3. Depositar
        4. Retirar 
        5. Salir 
        > ''')
        if opcion == '1':
            clients.append(register_client())
        elif opcion == '2':
            if not check_balance(clients):
                print('No existe un usuario con ese dni')
        elif opcion == '3':
            deposit(clients)
        elif opcion == '4':
            for client in clients:
                print(client.description())
        else:
            print('¡Adios!')
            break 
        
main()