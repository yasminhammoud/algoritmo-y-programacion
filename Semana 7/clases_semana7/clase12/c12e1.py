class Vehicle: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describe(self):
        return f'{self.brand}/{self.model}'
    
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        Vehicle.__init__(self, brand, model)
        self.doors = doors

    def describe(self):
        return f'{self.brand}/{self.model}/{self.doors}'

def main():
    vehicle = Vehicle('Brand', 'Model')
    car = Car('CarBrand', 'CarModel', 4)
    print(vehicle.describe())
    print(car.describe())

main()