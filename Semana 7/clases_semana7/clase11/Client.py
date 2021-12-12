class Client:

    bank = "Avila Bank"

    def __init__(self, name, dni, birthdate, gender, balance):
        self.name = name
        self.dni = dni
        self.birthdate = birthdate
        self.gender = gender
        self.balance = balance

    def my_balance(self):
        print(f'El balance del cliente {self.dni} es de {self.balance}')
    
    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        self.balance -= amount 
    
    def description(self):
        return 'Nombre: {}, Dni: {}, Nacimiento: {}, Genero: {} , Balance: {}'.format(self.name, self.dni, self.birthdate, self.gender, self.balance)