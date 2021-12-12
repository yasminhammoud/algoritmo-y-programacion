from Member import Member
from Professor import Professor
from Student import Student

def check_age():
    """[Devuelve la edad si cumple con las condiciones]

    Returns:
        [int]: [Edad]
    """
    while True:
        try:
            age= int(input('Ingrese la edad: '))
        except ValueError:
            print("Ingrese un número entero")
            continue
        if age not in range(1,135):
            print("Edad invalida")
        else:
            break
    return age

def check_carnet():
    """[Verifica si el usuario ingresa un carnet válido]

    Returns:
        [int]: [Carnet válido]
    """
    while True:
         try:
             carnet = int(input('Ingrese el carnet: '))
         except ValueError:
             print("Ingrese un secuencia de números")
             continue
         if (len(str(carnet))!=11):
             print("Carnet inválido")
         else:
             break
    return carnet

def register_member(members):
    """[Registra un nuevo miembro de la Unimet, verificando si es profesor o alumno,
        para así almacenar sus respectivos datos]

    Args:
        members ([list]): [Miembros de la Unimet sin el nuevo miembro]

    Returns:
        [list]: [Miembros de la Unimet con el nuevo miembro agregado]
    """
    while True:
        try:
            type_member = int(input("\nIngrese el número de la opción que desea elegir: \n1.Profesor\n2.Estudiante\n>"))
        except ValueError:
            print("Ingrese un número")
            continue
        if type_member>2 or type_member<1:
         print("\nEl número ingresado no forma parte de las opciones")
        else:
            break
    
    name = input("Ingrese su nombre: ").capitalize()
    while not name.isalpha():
        name = input("Ingrese un nombre: ").capitalize()
    age = check_age()
    email = input("Ingrese su correo: ")
    for member in members:
        while (member.email)==email:
            email = input("Correo existente! - Ingrese uno nuevo: ")
    carnet = check_carnet()

    if type_member==1:
        subject = input("Ingrese la(s) materia(s) que dicta: ").capitalize()
        member = Professor(name, age, email, carnet, subject)
        print("\n¡Profesor registrado con éxito!")
    elif type_member==2:
        career = input("Ingrese la(s) carrera(s) que cursa: ").capitalize()
        member = Student(name, age, email, carnet, career)
        print("\n¡Estudiante registrado con éxito!")
    
    members.append(member)
    return members

def access_info(members):
    """[Permite acceder a la información del miembro de la Unimet al ingresar 
        un correo que forme parte de la base de datos]

    Args:
        members ([list]): [Todos los miembros que forman parte de la Unimet]

    Returns:
        [list]: [Todos los miembros que forman parte de la Unimet]
    """
    email= input("Ingrese su correo: ")
    for member in members:
        if member.email == email:
            print(member.description())
            return True
    return False 

def eliminate_member(members):
    """[Elimina un miembro de la Unimet al ingresar el correo correspondido]

    Args:
        members ([list]): [Todos los miembros de la Unimet]

    Returns:
        [list]: [Todos los miembros de la Unimet menos el miembro eliminado]
    """
    email= input("Ingrese el correo del miembro de la Unimet que desea eliminar: ")
    for member in members:
        if member.email == email:
            members.remove(member) 
            print("\nMiembro eliminado")
            return members

def main():

    members = []

    while True:
        while True:
            try: 
                option = int(input(''' \n¡Bienvenido a la base de datos de los miembros de la Universidad Metropolitana!
                Ingrese el número correspondiente a la opción que desee accionar:
                1. Registrarse
                2. Ver información
                3. Eliminar miembro
                4. Salir
                > '''))
            except ValueError:
                print("Ingrese un número")
                continue
            if option not in range(1,5):
                print("Número fuera de rango")
            else:
                break 
        if option == 1:
            register_member(members)
        elif option == 2:
            if len(members)>0:
                access_info(members)
            else:
                print("No hay miembros registrados")
        elif option == 3:
            if len(members)>0:
                eliminate_member(members)
            else:
                print("No hay miembros registrados")
        else:
            print('¡Adios!')
            break 

main()
