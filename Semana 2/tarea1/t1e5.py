""" 
Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento en las entradas 
basado en la edad del cliente, para ello tendrás que recibir por teclado la edad y nombre del cliente y 
verificar los siguientes casos:

Si su edad es menor o igual a 4 años (`Free Ticket`) el precio de su entrada es gratis.
Si su edad es menor o igual a 12 (`Child Ticket`) el precio de su entrada es $2.
Si su edad es menor o igual a 18 años (`Teen Ticket`) el precio de su entrada es de $3
Si su entrada es menor a 60 años (`Adult Ticket`) el precio es de $5
Si su edad es mayor o igual a los 60 años (`Elder Ticket`) su entrada tendrá un valor de $2.5

También se darán descuentos adicionales solo a (Teen Ticket y Adult Ticket) siguiendo lo siguiente casos
    a. Si es Jueves o Lunes un 10% de descuento
    b. Si es estudiante un 20% de descuento

Solo se puede dar un descuento, siendo a el de mayor prioridad seguido de b.
Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su entrada.

Output esperado:
El cliente: {name} tiene: {age} años y su entrada de cine cuesta: ${price}, y tuvo un descuento de {discount}%
"""
name = input("Ingrese el nombre del cliente: ")
age = int(input("Ingrese la edad: "))
if age<=4:
 price=0 
 discount=0
elif 4<age<=12 :
  price=2
  discount=0
elif 12<age<=18 or 18<age<=60:
  dia = input("¿Es hoy lunes o jueves? Responda con un 'si' o 'no': ")
  if dia == 'si':
    discount=10
    if 12<age<=18: 
      price=2.7
    else:
      price=4.5
  elif dia == 'no': 
    estudiante = input("¿Es estudiante? Responda con un 'si' o 'no': ")
    if estudiante == 'si':
        discount=20
        if 12<age<=18:
            price=2.4
        else:
          price=4
    elif estudiante == 'no':
        discount=0
        if 12<age<=18:
            price=3
        else: 
            price=5
else:
  price=2.5
  discount=0
print(f"El cliente: {name} tiene: {age} años y su entrada de cine cuesta: ${price}, y tuvo un descuento de {discount}%")