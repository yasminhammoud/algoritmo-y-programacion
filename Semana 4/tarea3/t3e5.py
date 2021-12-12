# 5.  Escriba un programa que dada una matriz 3x3 determine si es invertible.

#Pista: Para que una matriz sea invertibles su determinante debe ser indistinto de 0.
#Nota: No pueden usar ninguna librería como numpy.

# a11 a12 a13        00 01 02
# a21 a22 a23        10 11 12   
# a31 a32 a33        20 21 22

#parachequear= ((m[0][0]*m[1][1]*m[2][2])+(m[1][0]*m[2][1]*m[0][2])+(m[2][0]*m[0][1]*m[1][2])-
#               (m[0][2]*m[1][1]*m[2][0])-(m[1][2]*m[2][1]*m[0][0])-(m[2][2]*m[0][1]*m[1][0]))

m = [
  [1, -1, 4],
  [2, 1, -1],
  [3, -1, 1]
]

suma=[]
resta=[]
for i in range(0,3):
  if i==0:
    suma.append(int((m[i][i]*m[i+1][i+1]*m[i+2][i+2])))
    suma.append(int((m[i+1][i]*m[i+2][i+1]*m[i][i+2])))
  if i==1:
    suma.append(int((m[i+1][i-1]*m[i-1][i]*m[i][i+1])))
    resta.append(int((m[i-1][i+1]*m[i][i]*m[i+1][i-1])))
  elif i==2:
    resta.append(int((m[i-1][i]*m[i][i-1]*m[i-2][i-2])))
    resta.append(int((m[i][i]*m[i-2][i-1]*m[i-1][i-2])))

determinante = sum(suma)-sum(resta)
print(determinante)
#if determinante != 0:
#  print('La Matriz es invertible')
#else:
#  print('La Matriz no es invertible')
