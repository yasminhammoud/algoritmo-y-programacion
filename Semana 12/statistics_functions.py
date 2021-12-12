import pickle
from cruises_functions import save_ship_information
from Client import Client
from Ship import Ship 
from Statistics import Statistics

def save_cruises_information(clients, ships):
    """[Guarda la información de las estadísticas como atributos de un objeto]

    Args:
        clients ([list]): [Lista con todos los clientes de la línea del crucero]
        ships ([list]): [Lista con la información de cada crucero (objetos)]

    Returns:
        [object]: [Objeto que tiene toda la información para las estadísticas]
    """

    total_sells = []
    client_with_no_tours = []
    ship1 = []
    ship2 = []
    ship3 = []
    ship4 = []

    if len(clients)>0:

        for client in clients:
            total_sells.append(client.moneySpent)
            if client.boughtTour == False:
                client_with_no_tours.append(1)
            if client.chosenCruise == ships[0].name:
                ship1.append(1)
            elif client.chosenCruise == ships[1].name:
                ship2.append(1)
            elif client.chosenCruise == ships[2].name:
                ship3.append(1)
            elif client.chosenCruise == ships[3].name:
                ship4.append(1)


        average_per_client = sum(total_sells)/len(clients)
        
        tour_percentage = (sum(client_with_no_tours)/len(clients))*100

        top_clients =  sorted(clients, key = lambda client: client.moneySpent, reverse=True)

        passanger_cruises = {'El Dios de los Mares': sum(ship1), 'La Reina Isabel': sum(ship2), 'El Libertador del Océano': sum(ship3), 'Sabas Nieves': sum(ship4)}
        top_ships = {ship: passangers for ship, passangers in sorted(passanger_cruises.items(), key = lambda x: x[1], reverse=True)}
                
        top_products = []
        for ship in ships:
            for sell in ship.sells:
                top_products.append((sell['name'],sell['amount']))

        top_products.sort(key=lambda product: product[1], reverse=True)

        saman_caribbean_statistics = Statistics(average_per_client, tour_percentage, top_clients, top_ships, top_products)
    else:
        print("No hay clientes registrados")
        
    return saman_caribbean_statistics

def file_existence(file_name):
    """[Verifica si el archivo existe o no]

    Returns:
        [bool]: [Dependiendo de la existencia del archivo]
    """
    try: 
        with open(file_name) as f:
            return True
    except FileNotFoundError as e:
        return False 

def statistics():
    """[Muestra la información del funcionamiento de la línea del crucero según lo que desee el usuario]
    """
    
    print("\n¡Bienvenido al módulo de estadísticas del Saman Caribbean!")
    ships_info = save_ship_information()
 
    while True:

        if file_existence("clients_information.txt"):
            with open("clients_information.txt", 'rb') as file:
                clients = pickle.load(file)
            saman_caribbean_statistics = save_cruises_information(clients, ships_info)
        else: 
            print("No se pueden ejecutar las funciones porque no hay datos registrados")
            break

        while True:
            try: 
                user_input = int(input("\n¿Qué desea saber del Saman Caribbean? \n1. Promedio de gasto de un cliente en el crucero \n2. Porcentaje de clientes que no compran tour \n3. Los primeros 3 clientes de mayor fidelidad \n4. Top 3 cruceros con más ventas de tickets \n5. Top 5 productos más vendidos en el restaurante \n6. Salir \n>>> "))
                if user_input not in range(1,7):
                    raise ValueError
                break
            except ValueError:
                print("Dato ingresado no forma parte de las opciones")

        if user_input==1:
            print(f"\nEl promedio de gasto de un cliente es: {saman_caribbean_statistics.averagePerClient}$")
            
        elif user_input==2:
            print(f"\nEl porcentaje de clientes que no compran Tours es: {saman_caribbean_statistics.tourPercentage}%")
        
        elif user_input==3:
            print("\nLos primeros 3 clientes de mayor fidelidad son:")
            for i in range(3):
                print(f"{i+1}. {((saman_caribbean_statistics.topClients)[i]).name}")

        elif user_input==4:
            print("\nLos Top 3 cruceros con más ventas de tickets son:")
            ships = [key for key in (saman_caribbean_statistics.topShips).keys()]
            for i in range(3):
                print(f"{i+1}. {ships[i]}")

        elif user_input==5:
            top_products = []
            for product in saman_caribbean_statistics.topProducts:
                if product[0] not in top_products:
                    top_products.append(product[0])
                    
            print("\nLos 5 productos más vendidos en el restaurante son:")
            for i in range(5):
                print(f"{i+1}. {top_products[i]}")

        else:
            print("¡Hasta luego!")
            break 


"""
from bokeh.charts import Bar, output_file, show

**TOP 3 CLIENTES**
output_file("lines.html")
names = [saman_caribbean_statistics.topClients)[i]).name for i in range(3)]
moneySpent = [saman_caribbean_statistics.topClients)[i]).moneySpent for i in range(3)]
top = Bar(data, title="Top 3 clientes de mayor fidelidad", xlabel = 'names', ylabel = 'moneySpent', width=400, height=400)
top.line (x, y, legend="Dinero gastado")
show(top)

**TOP 3 CRUCEROS**
output_file("lines.html")
tickets_sold = [value for value in (saman_caribbean_statistics.topShips).values()]
x = [ships[i] for i in range(3)]
y = [tickets_sold[i] for i in range(3)]
p = Bar(data, title="Top 3 cruceros con más ventas de tickets", xlabel = 'x', ylabel = 'y', width=400, height=400)
p.line (x, y, legend="Tickets vendidos")
show(p)

**TOP 5 PRODUCTOS**
top_products = []
for product in saman_caribbean_statistics.topProducts:
    if product[0] not in top_products:
        top_products.append(product[0])
        
top_amounts = []
for amount in saman_caribbean_statistics.topProducts:
    if amount[1] not in top_products:
        top_products.append(product[1])

products = [top_products[i] for i in range(5)]
amounts = [top_amounts[i] for i in range(5)]
sells = Bar(data, title="Top 5 productos más vendidos", xlabel = 'products', ylabel = 'amounts', width=400, height=400)
p.line (x, y, legend="Cantidad vendida")
show(sells)              
"""
