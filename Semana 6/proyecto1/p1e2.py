"""
Pregunta 2

Gracias por contribuir al problema anterior, nuestros científicos están más cerca de la cura, 
ahora necesitamos que nos ayuden con el siguiente problema, nuestro laboratorio de logística se 
encuentra investigando como distribuir la vacuna a aquellas personas que no tengan un suministro 
estable de agua potable las poblaciones rurales en africa. Para ello necesitan realizar un generador 
de números aleatorios que les permita realizar simular distintos escenarios posibles para ello, necesitan 
una subprograma que dada una secuencia de números determine cual es el numero de dicha secuencia que falta.

Input: [9,6,4,2,3,5,7,0,1]

Output: 8
"""

def missing_number(sequence):
    """
    Delvuelve el número o los números faltantes de la secuencia introducida
    
    Argument: 
    Sequence {list} -- Secuencia de números

    Return: 
    num {int} -- Número o números faltantes 
    """
    for num in range(min(sequence),max(sequence)):
        if num not in sequence:
            print(num)

def main():
    sequence = [9,6,4,2,3,5,7,0,1]
    missing_number(sequence)

main()
