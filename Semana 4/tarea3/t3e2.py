#2.  Escriba un programa de Python que imprima todos los valores únicos del diccionario classrooms.

#OUTPUT ESPERADO
#'SSL-02', 'SSL-04', 'SSL-01', 'SSL-03' #Si el output no te sale en el mismo orden no importa, dale a submit anyway
#

#classrooms = {"V": "SSL-01", "V": "SSL-02", "VI": "SSL-02", "VI": "SSL-03", "VII": "SSL-04", 
# "V": "SSL-01", "VIII": "SSL-04"}

classrooms = [{"V": "SSL-01"}, {"V": "SSL-02"}, {"VI": "SSL-02"}, {"VI": "SSL-03"}, {"VII": "SSL-04"}, {"V": "SSL-01"}, {"VIII": "SSL-04"}]
unique_class = set()
for classroom in classrooms:
    for seccion in classroom:
        unique_class.add(classroom[seccion])
print(unique_class)