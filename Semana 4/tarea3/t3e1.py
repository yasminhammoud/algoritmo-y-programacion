#1. Escriba un script de Python para imprimir un diccionario donde 
#   las claves son números entre 1 y 15 (ambos incluidos)  y 
#   los valores son los cuadrados de sus claves.

num_cuadrados = {}
for i in range(1,16):
    num_cuadrados[i]= i**2    
print(num_cuadrados)

#OUTPUT ESPERADO: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


