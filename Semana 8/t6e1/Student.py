from Member import Member

class Student(Member): 
    def __init__(self, name, age, email, carnet, career):
        super().__init__(name, age, email, carnet)
        self.career = career
    
    def description(self):
        return (f'\nNombre del estudiante: {self.name}\nEdad: {self.age}\nCorreo: {self.email}\nCarnet: {self.carnet}\nCarrera(s) que estudia: {self.career}')