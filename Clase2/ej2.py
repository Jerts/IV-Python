a = int(input("Ingresa el coeficiente a: \n"))
b = int(input("Ingresa el coeficiente b: \n"))
c = int(input("Ingresa el coeficiente c: \n"))

root_1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
root_2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)

print(f'La primera raiz es: {root_1}')
print(f'La segunda raiz es: {root_2}')
