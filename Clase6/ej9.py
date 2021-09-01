def f(x):
    return x**2

x_l_c = [i for i in range(0,11)]
y_l_c = [f(x) for x in range(0,11)]

filename = "datosXY.csv"
new_file = open(filename,'w')
for i in range(len(x_l_c)):
    new_file.write(f'{x_l_c[i]},{y_l_c[i]}\n')
new_file.close()