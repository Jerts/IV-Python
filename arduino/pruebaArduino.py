import serial
import matplotlib.pyplot as plt
from drawnow import *
import time

data = []
t = []

#Puerto del NODEMCU ESP32
serial_port = "COM4"

arduino_data = serial.Serial(serial_port,9600)

def make_fig():
    plt.title("Lectura de la terminal analógica en el ADC1 CH0")
    plt.ylim(-0.1,6)
    plt.grid(True)
    plt.xlabel("Tiempo (s) ", fontsize=18)
    plt.ylabel("Tension (V)", fontsize=18)
    plt.plot(t,data,'ro--')

N=200

for i in range(N):
    try:
        data_str = arduino_data.readline()
        string_data = str(data_str.decode('cp437'))
        string_data = string_data.replace("\n",'')
        temp_data = float(string_data)*(5/4095)
        data.append(temp_data)
        t.append(i*0.1)
        drawnow(make_fig)
        print(string_data)
    except:
        print('Chagefeó tu medida, bro!')

arduino_data.close()

filename = "datosArduino.csv"
new_file = open(filename,'w')
for i in range(len(data)):
    new_file.write(str(t[i]+','+str(data[i])+'\n'))
new_file.close()