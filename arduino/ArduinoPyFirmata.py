






from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT
import time
import matplotlib.pyplot as plt
from drawnow import *

def make_fig():
    plt.title("Lectura de la terminal analógica en el ADC1 CH0")
    plt.ylim(-0.1,6)
    plt.grid(True)
    plt.xlabel("Tiempo (s) ", fontsize=18)
    plt.ylabel("Tension (V)", fontsize=18)
    plt.plot(t,data,'ro--')

port = "COM3"
board = Arduino(port)
it = util.Iterator(board)
it.start()
board.digital[13].mode = OUTPUT
board.analog[0].mode = INPUT
time.sleep(2)
board.analog[0].enable_reporting()
data = []
t = []
temp_t = 0
N = 10
for i in range(N):
    if (i%2==0):
        board.digital[12].write(1)
    else:
        board.digital[12].write(0)
    if (i==0):
        print('Tiempo (s)\tTension(V)')
    try:

        p = board.analog[0].read()
        p=p*5.0
        time.sleep(0.5)
        data.append(p)
        t.append(temp_t)
        print("%g \t %g"%(temp_t,p))
        temp_t=temp_t+0.5
        drawnow(make_fig)
    except:
        print('Mala medida')
board.analog[0].disable_reporting()
board.digital[12].write(0)
board.exit()

filename = "datosArduino.csv"
new_file = open(filename,'w')
for i in range(len(data)):
    new_file.write(str(t[i]+','+str(data[i])+'\n'))
new_file.close()