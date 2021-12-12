""" 
Construye un programa que, al recibir como datos los tres lados de un triángulo, calcule e imprima su área. 

Input de prueba:
L1 = 1
L2 = 2
L3 = 3

Output esperado: 
El área del triangulo es: 0
"""

l1 = float(input("Ingrese el primer lado del triángulo: "))
l2 = float(input("Ingrese el segundo lado: "))
l3 = float(input("Ingrese el tercer lado: "))
aux = (l1 + l2 + l3)/3
area = ((aux*(aux-l1)*(aux-l2)*(aux-l3))**0.5)
print(f"El área del triángulo es: {area}")