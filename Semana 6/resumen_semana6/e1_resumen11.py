def is_primenumber(number):
    if num > 1:
        for i in range(2,numbers):
            if (numbers % i) == 0:
                return print(numbers,"No es un número primo")
                break
            else:
                return numbers
    else:
        print(f '{num} no es un número entero o {} es igual a 1')
                  
def main():
    num = int(input('Introduzca un numero: '))
    if is_primenumber(num)==num:
        mersenne_prime = (2**num)-1 
        if is_primenumber((2**num)-1) == mersenne_prime: 
            print("Es un numero mersenne primo")
        elif mersenne_prime != is_primenumber(mersenne_prime):
            print("No es un número mersenne primo")

main()