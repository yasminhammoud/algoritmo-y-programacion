#3. Escriba un programa Python para crear y mostrar todas las combinaciones de letras, 
#   seleccionando cada letra de una clave diferente en el diccionario data.

#OUTPUT ESPERADO:
#a b
#a c
#a d
#b c
#b d
#c d

data =  {'1':['a','b'], '2':['c','d']}

data_list = []
for key in data:
    for i in range(len(key)+1):
        data_list.append(data[key][i])
for i in range(len(data_list)):
    for j in range(i):
        last_letter= data_list[i]
        first_letter=data_list[j]
        if first_letter!=last_letter:
            for first in first_letter:
                for last in last_letter:
                    print(first,last)

#combination = [(x, y) for idx, x in enumerate(data_list) for y in data_list[idx + 1]]


#data =  {'1':['a','b'], '2':['c','d']}
#data_list = []
#for key in data: 
#    for i in range(len(data[key])):
#        data_list.append(data[key][i])
#        combinaciones = [(x,y) for x in data_list for y in data_list if x!=y and (x,y)!=(y,x)]
#print(combinaciones)


#data =  {'1':['a','b'], '2':['c','d']}
#data_list = []

#    data_list.append(data['1'])
 #   data_list.append(data['2'])
  #  print(data_list)
        
        
#        for first in data_list:
#            for last in data_list:
#                if first!=last:
#                    print(first,last)
