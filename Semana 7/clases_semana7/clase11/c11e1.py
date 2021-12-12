class Vehicle:
    seller = 'Avila Cars C.A.'

    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    
    def show_attr(self):
        return 'Marca: {}, Modelo: {}, Color: {}, Año {}'.format(self.brand, self.model, self.color, self.year)

def main():
    corolla = Vehicle("Toyota", "Corola", "Gris", 2015)
    print(corolla.show_attr())
    corolla.color = "White"
    print(corolla.show_attr())

    tesla_x = Vehicle("Tesla", "X", "Negro", 2019)
    print(tesla_x.show_attr())
    tesla_x.color = "Blanco"
    print(tesla_x.show_attr())

main()

