#Ejercicio 4

#A la clase de Estructuras de Datos del profesor Guillén asiste un grupo numeroso de alumnos. 
#El profesor Guillén es muy exigente y aplica cuatro exámenes durante el trimestre. 
#Escribe un programa que resuelva lo siguiente:


#El promedio de calificaciones de cada alumno.
#El promedio del grupo en cada examen.
#El examen que tuvo el mayor promedio de calificación

#El promedio del alumno: 1 es : 14.5 
#El promedio del alumno: 2 es : 9.0 
#El promedio del alumno: 3 es : 10.75 
#El promedio del alumno: 4 es : 10.75 
#El promedio del alumno: 5 es : 9.75  

#El Promedio del Examen: 1 fue: 10.0 
#El Promedio del Examen: 2 fue: 9.0 
#El Promedio del Examen: 3 fue: 14.6 
#El Promedio del Examen: 4 fue: 10.2  

#El examen con el promedio mas alto fue: 3 y el promedio: 14.6 

data = [
[18, 10, 16, 14],   
[10,  6, 13,  7],   
[ 7, 12, 15,  9],   
[ 3,  9, 12, 19],   
[12,  8, 17,  2], 
]

promedio_alumno = {}
prom_exam=[0,0,0,0]
promedio_examen = {}

for i in range(len(data)):
    promedio_alumno[i+1]=sum(data[i])/len(data[i])
    for j in range(len(data[i])):
        prom_exam[j] += data[i][j]

for i in range(len(prom_exam)):
    promedio_examen[i+1]=prom_exam[i]/5
    highest_score = max(prom_exam)/5
    best_exam= prom_exam.index(max(prom_exam))+1 

for alumno, promedio in promedio_alumno.items():
    print("El Promedio del alumno: {} es: {}".format(alumno,promedio))
print()
for exam, average in promedio_examen.items():
    print("El Promedio del Examen: {} fue {}".format(exam,average))
print()
print(f'El examen con el promedio más alto fue: {best_exam} y el promedio: {highest_score}')