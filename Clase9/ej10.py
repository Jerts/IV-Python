import matplotlib.pyplot as plt
import numpy as np
filename = "Datos2.csv"
new_file = open(filename,'r')
data_str = []
for line in new_file:
    line=line.replace('\n',"")
    data_str.append(line.split(","))

new_file.close()