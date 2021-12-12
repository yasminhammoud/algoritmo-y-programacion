from abc import ABC, abstractmethod 

class Member(ABC):
    def __init__(self, name, age, email, carnet):
        self.name = name
        self.age = age
        self.email = email
        self.carnet = carnet
        
    @abstractmethod
    def description(self):
        pass