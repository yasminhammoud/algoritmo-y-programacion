from Animal import Animal
from Pig import Pig
from Cow import Cow
from Sheep import Sheep 

def main():
    print("""¡Bienvenido! \nIngrese la cantidad de animales que hay en cada sección de la granja""")
    while True:
        try:
            amount_pig = int(input("Cantidad de cochinos: "))
            amount_cow = int(input("Cantidad de vacas: "))
            amount_sheep = int(input("Cantidad de ovejas: "))
        except ValueError:
            print("Ingrese un número entero")
            continue
        if amount_cow<0 or amount_pig<0 or amount_sheep<0:
            print("Ingrese un número entero positivo")
        else:
            break 
    
    pig = Pig(amount_pig, 2)
    cow = Cow(amount_cow, 3)
    sheep = Sheep(amount_sheep, 1)
    
    cow.milk_cow()
    print("\nLa cantidad de alimentos consumida por cada tipo de animal fue:")
    pig.food_eaten()
    cow.food_eaten()
    sheep.food_eaten()
    pig.bath_water_spent()

main()





