from Animal import Animal

class Cow(Animal):

    def __init__(self, amount, kg_food):
        super().__init__('Vacas', amount, kg_food)
    
    def milk_cow(self):
        return print("\nLas vacas fueron ordeñadas por el día de hoy")

 