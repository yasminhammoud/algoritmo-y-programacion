"""def max_area(coordinates):
  pass

def main():
  coordinates = [1,8,6,2,5,4,8,3,7]
  print(max_area(coordinates))

main()

Bienvenido a La Julia Labs, en estas instalaciones de alta tecnología estamos desarrollando la vacuna XDE-12,
la cual promete ser una solución para la pandemia del COVID-19. Estamos muy cerca de dar con la vacuna, 
sin embargo, necesitamos realizar un procesamiento de datos importante para terminar de solucionar el problema 
y poder patentar la vacuna, salvar la humanidad y ganarle a la competencia.

Para cumplir este objetivo necesitamos de tu ayuda de manera urgente, tu labor sera solucionar los siguientes problemas utilizando 
técnicas de automatización y todos tus conocimiento de programación con Python.

Pregunta 1
Actualmente en nuestros laboratorios realizamos un ensayo sobre la capacidad de disolución de nuestra vacuna en agua para saber 
si es posible vacunar a mas gente a traves de los sistemas hidráulicos mundiales. Una de las variables para determinar esto es 
el area del contenedor en donde se disuelve la vacuna, los científicos han guardado la información de este experimento en una lista 
de n posiciones en donde cada elemento de la lista indica la altura del contenedor y la posición en la lista indica su valor en el 
eje X, en el lenguaje matemático esto se ve representado como una sucesión de ai elementos, donde el par ordenado (i, ai) representa 
un plan en el plano x,y, su tarea es encontrar un par de coordenadas (x,y) tales que se máxime el area del contenedor. Los científicos
ya han desarrollado gran parte del programa para el análisis de datos y les falta la implementación de la función la cual es su tarea.

Output:   49

Las coordenadas de las barras rojas son (1, 8) para la primera y(8, 7) 
para la segunda, la distancia horizontal es 8-1 = 7 y la altura es 7, 7*7 = 49 
"""

def max_area(coordinates):
    """ 
    Devuelve el area máxima calculada con las ordenadas de la lista introducida y sus respectivos valores de x 
    
    Arguments: 
    coordinates {list} : Lista de las ordenadas (y)
    
    Returns: 
    max(area) {int} : area maxima  conseguida con la multiplicación de x*y 
    """
    if len(coordinates)<2: 
      return print("Lista introducida tiene un tamaño menor que 2")
    elif 2<=len(coordinates):
      coordinates_x = [(i) for i in range(len(coordinates)) if 2<=len(coordinates)]
      area = [((x-1)*coordinates[x]) for x in coordinates_x]
      return max(area)

def main():
    coordinates = [1,8,6,2,5,4,8,3,7]
    print(max_area(coordinates))

main()

