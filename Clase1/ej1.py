# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 2021
"""
from math import pi
#print("Ingresa un angulo en grados: ")
deg_ang = float(input("Ingresa un angulo \n"))
red_ang= deg_ang* (pi/180)

print("%g grados corresponde a %g radianes" %(deg_ang,red_ang))