"""
Problema 3 

Ya estamos muy cerca, el Centro de Control de Enfermedades (CDC) ha aprobado nuestros estudios en primates, y
 nos ha autorizado a hacer la prueba con humanos, para ello necesitamos tu apoyo, tu última tarea sera desarrollar 
 una aplicación que permita registrar a todas las personas que se involucran en nuestras pruebas y controlar los gastos 
 de la compañía ya que a estas personas hay que pagarles por su participación.

Por cada nueva persona que ingrese al estudio es necesario conocer los siguientes datos:

    Edad (si es menor de 21 años no puede participar) 
    Genero (Masculino o Femenino) 
    Peso (Si es hombre su peso debe debe ser mayor a 55 kg y si es mujer debe ser mayor a 45kg) 
    Altura 
    Condición Medida Preexistente (Asmático, Hipertensión, Ninguna) 


Todas las personas recibirán un pago base de 8000 USD, sin embargo, existen algunos recargos presentados a continuación:

    Si la persona es mayor a 60 años se le recargara un 10% 
    Si la persona es Asmática se le pagara un 30% adicional 
    Si la persona es Hipertensa se le pagara un 20% adicional. 


Después, de Ingresar todos los datos, la persona es informada con los riesgos y el monto a pagarle y ella decide si ingresa al estudio o no. 
Durante la elaboración de los estudio hay un probabilidad de 1:10 (0.1) de que un paciente tenga una complicación.

Después de realizar todos los estudios diarios, la compañía necesita saber la siguiente información:

    La cantidad de pacientes que aceptaron el estudio 
    La cantidad de pacientes que rechazaron el estudio 
    La cantidad neta de dinero a pagar 
    La cantidad de recargos otorgados 
    La cantidad total pagar 
    El promedio de pago a los hombres 
    El promedio de pago a las mujeres 
    Los pacientes con complicaciones 


nota *: Para simular la probabilidad utilice la librería random de python si random.random() <= 0.1 entonces el paciente se complico.  
"""
import random
random.seed(42)

def patient_age():
    """
    Devuelve la edad si cumple con las condiciones 
    
    Returns: 
    age {int} -- Edad
    """
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

def patient_gender():
    """
    Devuelve el género si cumple con las condiciones 

    Returns: 
    gender {str} -- Género
    """
    while True: 
        try: 
            gender = input("¿Es de género Masculino o Femenino? Ingrese 'M' o 'F': ").upper() 
            if gender =='F' or gender =='M':
                break 
        except:
            pass
    return gender

def patient_weight():
    """
    Devuelve el peso si cumple con las condiciones 

    Returns: 
    weight {float} -- Peso 
    """
    while True:
        try:
            weight = float(input('Ingrese el peso en kilogramos: '))
        except ValueError:
            print("El peso debe ser un número")
            continue
        if weight<20 or weight>600:
            print("Peso no valido")
        else:
            break
    return weight

def patient_height():
    """
    Devuelve la altura si cumple con las condiciones 
    
    Returns: 
    height {float} -- Altura
    """
    while True:
        try:
            height = float(input('Ingrese la altura en metros: '))
        except ValueError:
            print("La altura debe ser un número")
            continue
        if height<0.25 or height>3.0:
            print("Altura no valida")
        else:
            break
    return height

def preeexitent_medical_condition():
    """
    Devuelve la condición médica pre-existente de la persona 

    Returns: 
    condition {str} -- 'A': Asmático, 'H': Hipertensión, 'N': Ninguna
    """
    while True: 
        try: 
            condition = input("Si es asmático, ingrese 'A'; si tiene hipertensión, 'H'; si no tiene ninguna condición, 'N': ").upper() 
            if condition =='A' or condition =='H' or condition =='N': 
                break 
        except:
            pass
    return condition

def monto_total(age, condicion_medica):
    """
    Devuelve los pagos adicionales del paciente según los datos introducidos por el mismpo 

    Arguments:
    age {int} -- Edad del paciente 
    condicion_medica {str} -- Asmático o con Hipertensión o Ninguno

    Returns: 
    bonus_age {int} -- Pago adicional si es mayor de 60 años
    bonus_a {int} -- Pago adicional si es asmático
    bonus_h {int} -- Pago adicional si tiene hipertensión

    """
    if age>60:
        bonus_age = int(8000*0.1)
    else: 
        bonus_age = 0
    if condicion_medica == 'A':
        bonus_a = int(8000*0.3)
    else:
        bonus_a = 0
    if condicion_medica == 'H':
        bonus_h = int(8000*0.2)
    else:
        bonus_h = 0 
    return  (bonus_age, bonus_a, bonus_h)

def patient_answer():
    """
    Devuelve la respuesta del paciente 

    Returns:
    acceptence_rejection {str} -- Input aprobado 
    """
    while True:
        try:
            acceptence_rejection = input("¿Desea realizar la prueba? Ingrese 's' para si , y 'n' para no: ").lower()
            if acceptence_rejection =='s' or acceptence_rejection =='n':
                break
        except:
            pass
    return acceptence_rejection

def patient_complications():
    """
    Returns: 
    Bool -- si el paciente tuvo una complicación o no 
    """
    complicacion = False 
    if random.random() <= 0.1:
        complicacion = True 
    return complicacion

def patient_registration(masculine_patient, feminine_patient, total_extra_payment, rejected_trial, total_payment_fem, total_payment_mas, complicacion_paciente):
    """
    Se encarga de hacerle una serie de preguntas al usuario, para así registrar exitosamente las respuestas de los pacientes 
    Arguments:
    Todas las listas del main

    Returns: 
    Las listas con los datos actulizados 

    """
    user_continue = 'si'
    print("¡Bienvenido!. Acaba de acceder a la base de datos del registro de los pacientes para las pruebas contra el COVID.")
    while user_continue == 'si':
        edad = patient_age()
        if edad>=21:
            genero = patient_gender()
            if genero == 'F':
                if patient_weight()>45:
                    patient_height()
                    condicion_medica = preeexitent_medical_condition()
                    (d_age, b_a, b_h) = monto_total(edad, condicion_medica)
                    amount_recieved = 8000+d_age+b_a+b_h
                    print(f'Conociendo los riesgos que implican estas pruebas, y el monto recibido por hacerlas, que en su caso sería {amount_recieved}$')
                    answer = patient_answer()
                    if answer == 's':
                        print("¡Bienvenido! Estaremos en contacto")
                        feminine_patient.append(1)
                        total_payment_fem.append(amount_recieved)
                        extra_payment = (d_age + b_a + b_h)
                        total_extra_payment.append(extra_payment)
                        complicacion = patient_complications()
                        if complicacion == True:
                            complicacion_paciente.append(1) 
                    elif answer == 'n':
                        print('Gracias por responder')
                        rejected_trial.append(1)
                else:
                    print("Para participar, el peso de la mujer debe ser mayor a 45kg") 
            elif genero == 'M':
                if patient_weight()>55:
                    patient_height()
                    condicion_medica = preeexitent_medical_condition() 
                    (d_age, b_a, b_h) = monto_total(edad, condicion_medica)
                    amount_recieved = 8000+d_age+b_a+b_h
                    print(f'\nConociendo los riesgos que implican estas pruebas, y el monto recibido por hacerlas, que en su caso sería {amount_recieved}$')
                    answer = patient_answer()
                    if answer == 's':
                        print("¡Bienvenido! Estaremos en contacto")
                        masculine_patient.append(1)
                        total_payment_mas.append(amount_recieved)
                        extra_payment = (d_age + b_a + b_h)
                        total_extra_payment.append(extra_payment)
                        complicacion = patient_complications()
                        if complicacion == True:
                            complicacion_paciente.append(1)
                    elif answer == 'n':
                        print('Gracias por responder')
                        rejected_trial.append(1)
                else:
                    print("Para participar, el peso del hombre debe ser mayor a 55kg")           
        else:
            print("La persona no puede participar porque es menor de 21 años")
        user_continue = input("\nSi desea continuar ingrese 'si', en caso contrario ingrese cualquier tecla: ").lower()
    return masculine_patient, feminine_patient, total_extra_payment, rejected_trial, total_payment_fem, total_payment_mas, complicacion_paciente

def main():
    masculine_patient = [0]
    feminine_patient = [0]
    total_extra_payment = [0] 
    rejected_trial = [0] 
    total_payment_fem = [0]
    total_payment_mas = [0] 
    complicacion_paciente = [0]
    (masculine_patient, feminine_patient, total_extra_payment, rejected_trial, total_payment_fem, total_payment_mas, complicacion_paciente) = patient_registration(masculine_patient, feminine_patient, total_extra_payment, rejected_trial, total_payment_fem, total_payment_mas, complicacion_paciente)

    acceptence_trial = sum(masculine_patient) + sum(feminine_patient)
    total_payment = sum(total_payment_fem) + sum(total_payment_mas)
    neta_total_payment = total_payment - sum(total_extra_payment)

    print(f'\nLa cantidad de pacientes que aceptaron el estudio fue: {acceptence_trial}')
    print(f'La cantidad de pacientes que rechazaron el estudio fue: {sum(rejected_trial)}')
    print(f'La cantidad neta de dinero a pagar es {neta_total_payment}$')
    print(f'La cantidad de recargos otorgados es {sum(total_extra_payment)}$')
    print(f'La cantidad total para pagar es {total_payment}$')
    if sum(feminine_patient)>0:
        fem_avarage_payment = sum(total_payment_fem)/sum(feminine_patient)
        print(f'El promedio de monto_total a las mujeres es: {fem_avarage_payment}$')
    else:
      print("No hay datos de la población femenina")
    if sum(masculine_patient)>0:
        mas_average_payment = sum(total_payment_mas)/sum(masculine_patient)
        print(f'El promedio de monto_total a los hombres es: {mas_average_payment}$')
    else:
      print("No hay datos de la población masculina")
    print(f'La cantidad de pacientes con complicaciones es: {sum(complicacion_paciente)}\n')

main()


