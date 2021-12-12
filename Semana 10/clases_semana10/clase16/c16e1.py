def linear_search(numeros, num):
    for i in range(len(numeros)):
        if numeros[i] == num:
            return True 
    return False

def binary_search(numeros, num):
    first = 0 
    last = len(numeros)-1
    index = -1 
    while (first <= last) and (index == -1):
        print('flag')
        mid = (first+last)//2 
        if numeros[mid] == num:
            return True
        else: 
            if num<numeros[mid]:
                last = mid-1
            else: 
                first = mid+1
    return False 

def main():
    
    numeros = [1,2,4,6,8,20,40,60,80]
    num = 2

    if binary_search(numeros, num):
        print("¡Número encontrado!")
    else:
        print("Número NO encontrado")
    
main()