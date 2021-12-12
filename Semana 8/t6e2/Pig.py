from Animal import Animal 

class Pig(Animal):

    def __init__(self, amount, kg_food):
        super().__init__('Cochinos', amount, kg_food) 

    def bath_water_spent(self):
        water_spent = 10 
        return print(f"\nLos cochinos ya fueron bañados, y la cantidad de agua consumida fue: {(self.amount)*water_spent} litros\n")