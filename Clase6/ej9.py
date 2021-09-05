import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def f(x):
    return x**2

x_l_c = [i for i in range(0,11)] #x lista de comprención
y_l_c = [f(i) for i in range(0,11)]

x_lista = []
y_lista = []
for i in range(11):
    x_lista.append(i)
    y_lista.append(f(i))

filename = "datosXY.csv"
new_file = open(filename,"w")
for i in range(len(x_lista)):
    new_file.write(str(x_lista[i]) + "," + str(y_lista[i])+"\n")
new_file.close()

#Abrir archivo
abrir = open(filename,"r")
data_str = []
for linea in abrir:
    print(linea)
abrir.close()
    
abrir = open(filename,"r")
data_str = []
for linea in abrir:
    linea = linea.replace("\n", "")
    data_str.append(linea.split(","))

abrir.close()
print(data_str)

#Por la forma compleja
#data_str a valores flotantes
data_float = []
for i in range(len(data_str)):
    list_t = [] #lista temporal
    for j in range(len(data_str[0])):
        list_t.append(float(data_str[i][j]))
    data_float.append(list_t)
print(data_float)

#La forma intermedia
data_lc = [[float(data_str[i][j]) for j in range(len(data_str[0]))] for i in range(len(data_str))]
 #data lista de comprencion
print(data_lc)

#La forma sencilla
import numpy as np
data_numpy = np.asarray(data_str, dtype=float)

#Método largo para obtener valores de x
x_dato_lc =[]
y_dato_lc = []
for i in range(len(data_float)):
    x_dato_lc.append(data_float[i][0])
    y_dato_lc.append(data_float[i][1])

# Otra forma es por la matriz transpuesta
def Mtranspuesta(a):
    m = len(a) #Renglones matriz A
    n = len(a[0]) #Columnas matriz A
    transpuesta = [[0 for i in range(m)] for i in range(n)]
    #print(transpuesta)
    for i in range(n):
        for j in range(m):
            transpuesta[i][j] = a[j][i]
    return(transpuesta)

MT = Mtranspuesta(data_float)
datos_x = MT[0] #primer renglon
datos_y = MT[1]

#Metodo con numpy
datos_numpy = data_numpy.T #T es la transpuesta
datos_x_numpy = datos_numpy[0]
datos_y_numpy = datos_numpy[1]

plt.figure()
ax=plt.axes()
ax.plot(datos_x,datos_y, 'C1o--')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title(r'$y=x^2$')