from Member import Member

class Professor(Member):
    def __init__(self, name, age, email, carnet, subject):
        super().__init__(name, age, email, carnet)
        self.subject = subject
    
    def description(self):
        return (f'\nNombre del profesor: {self.name}\nEdad: {self.age}\nCorreo: {self.email}\nCarnet: {self.carnet}\nMateria(s) que dicta: {self.subject}')
