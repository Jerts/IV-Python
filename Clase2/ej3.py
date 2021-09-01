n = int(input("Ingresa el numero entero para calcular el factorial \n"))
factorial = 1
if n==0 or n==1:
    factorial=1
else:
    for i in range(2,n+1):
        factorial *= i

print(f'n!={factorial}')