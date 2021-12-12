""" 
En las olimpíadas de invierno el tiempo que realizan los participantes en la competencia de velocidad 
en pista se mide en minutos, segundos y centésimas. La distancia que recorren se expresa en metros. 
Construye un programa que calcule la velocidad de los participantes en kilómetros por hora de las 
diferentes competencias. 

Nota: 1 segundo son 100 centésimas de segundos.

Input:

Por favor ingrese los minutos: 2
Por favor ingrese los segundos: 30
Por favor ingrese las centésimas: 15
Por favor ingrese la distancia en metros: 200

Output Esperado:

La velocidad en km/h es: 4.790419161676647
"""
min = int(input("Por favor ingrese los minutos: "))
seg = int(input("Por favor ingrese los segundos: "))
centiseg = int(input("Por favor ingrese las centesimas: "))
metros = int(input("Por favor ingrese la distancia en metros: "))
tiempo_hora = ((min/60)+(seg/(3600))+(centiseg/360000))
distancia_km = (metros/1000)
print(f"La velocidad en km/h es: {distancia_km/tiempo_hora}")