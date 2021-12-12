from Animal import Animal  

class Sheep(Animal):

    def __init__(self, amount, kg_food):
        super().__init__('Ovejas', amount, kg_food)

    