class Animal:

    def __init__(self, name, amount, kg_food):
        self.name = name 
        self.amount = amount
        self.kg_food = kg_food
    
    def food_eaten(self):
        return print(f" {self.name}: {(self.amount)*(self.kg_food)} kg")
 