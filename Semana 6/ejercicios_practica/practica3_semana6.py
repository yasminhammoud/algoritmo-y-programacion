La Unidad de Radiología de una Clínica en Caracas, ofrece varios Estudios a sus clientes. Los Estudios son de tres tipos:
​
Estudio Descripción Valor en Bs. x Estudio
​
U Ultrasonido 8.900 + (Edad\*1000)
T Tomografía 12.640 + (Edad\*1000)
R Resonancia 15.600 + (Edad\*1000)
​
Cuando el Cliente, solicita un Estudio en la Unidad de Radiología, se le solicitan los siguientes datos: 
Cedula de Identidad, Edad, Sexo (F=Femenino; M=Masculino, si pertenece a un seguro y el Tipo de Estudio (uno solo por cliente) 
que se le va a efectuar. Si la persona pertenece a un seguro se le aplicara un descuento del 80%. Si el cliente es Femenino y 
mayor de 70 años se le aplicara un 20% de descuento adicional. Si es Masculino y mayor de 80 se le aplicara un 15% de descuento adicional
​
def check_cedula(cedula):
    while True: 
        try:
            cedula = int(input("Ingrese la cédula de identidad: "))
        except ValueError: 
            print("Debes ingresar un número")
            continue 
        if cedula<0:
            print("Ingresa un número positivo")
        elif len(str(cedula))<6 or len(str(cedula))>8 or cedula>35000000:
            print("Cédula invalida")
            continue
        else:
            break 
    return cedula

def check_age(age):
    while True:
        try:
            age= int(input('Ingrese la edad: '))
        except ValueError:
            print("Ingrese un número entero")
            continue
        if age<0 or age>130:
            print("Edad invalida")
        else:
            break
    return age

def check_sex(sex):
    while True:
        try: 
            sex = input("¿Es de sexo Masculino o Femenino? Ingrese 'M' o 'F': ").upper()
        except sex !='F' or sex !='M':
            print("Ingrese 'F' o 'M'")


def datos(clientes, cedula):


        sex = input("¿Es de sexo Masculino o Femenino? Ingrese 'M' o 'F': ").upper()
        if sex =='F' or sex =='M':
            age = input('Ingrese la edad: ')
            if age.isnumeric(): 
                if sex == 'm' and int(age)>18:
                    mas_weight.append(float(weight))
                    mas_height.append(float(height)) 
                if sex == 'f' and int(age)>18:
                    fem_height.append(float(height))
                    fem_weight.append(float(weight))
            else:
                print(f' "{age}" no es un número')
        
    else:
        print('Dato invalido')

1. Para cada Cliente, el Programa deberá Desplegar la Información del Recibo con los siguientes datos:
​
El número de su cédula de identidad
Su Edad
El Código del Sexo
El Tipo de Estudio
Si pertenece a un seguro o no
El Monto Neto a Pagar, habiéndole aplicado el descuento para los casos que aplique.
​
2. Al final del Día.
​
def main():
clientes = []
    print(f'La cantidad de Clientes por tipo de Estudio {}')
    print(f'El Monto Total de Descuentos Otorgados')
    print(f'El Monto Total Neto Facturado')
    print(f'El Promedio de Pago de todos los Clientes')
    print(f'El promedio de pago por tipo de estudio')
    print(f'El cliente que recibió más descuento')
    print(f'El cliente que menos pago')

main()

#user_continue = 'si'
#while user_continue == 'si':
#    user_continue = input('¿Desea continuar? "si" o "no": ').lower()