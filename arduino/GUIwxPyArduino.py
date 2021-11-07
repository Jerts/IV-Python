# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:40:33 2021

@author: ross_
"""

import wx
import winreg
import itertools
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import  Figure
import numpy as np
import serial
import time
import glob
import sys

from wx.core import TextUrlEvent

class TopPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.axes.set_xlabel("Time (s)") 
        self.axes.set_ylabel("Voltage (V)")
        self.axes.set_ylim(-0.1,5.1)
        self.canvas.draw()
    def draw(self,x,y):
        self.axes.clear()
        self.axes.set_xlabel("Time (s)")
        self.axes.set_ylabel("Voltage (V)")
        self.axes.plot(x,y,'C1o--')
        self.canvas.draw()

class BottomPanel(wx.Panel):
    def __init__(self, parent, top):
        super().__init__(parent)
        self.graph = top
        self.btn_start = wx.Button(self, id=1, label="start",pos=(400,40))
        self.btn_stop = wx.Button(self, id=2, label="stop",pos=(400,40))
        self.btn_start.Bind(wx.EVT_BUTTON,self.on_button_start)
        self.btn_stop.Bind(wx.EVT_BUTTON,self.on_button_stop)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.time_interval, self.timer)
        self.lbl_comm_port = wx.StaticText(self,label="COM Port:",pos = (40,20))
        self.comm_port=wx.ListBox(self, id=3, pos=(40,40),choices=self.serial_ports()+['COM3'],style=0, name="Ports")
        print(self.serial_ports())
        self.lbl_samples=wx.StaticText(self, label = "samples", pos=(190,20))
        self.spin_ctrl_samples = wx.SpinCtrl(self, id=4, value="", pos=(190,40),min=1,max=1000,initial = 1,name="wxSpinCtrlSamples")
        self.btn_save_data = wx.Button(self, id=5, label="save", pos=(500,40),name="btnSaveData")
        self.btn_save_data.Bind(wx.EVT_BUTTON,self.on_button_save)
        self.btn_save_data.Hide()
        self.btn_stop.Hide()
        self.n=0
        self.serial_connection = False
        self.x = np.array([])
        self.y = np.array([])
        self.values = []
        self.stop_acquisition = False
        self.high_value_board = 5.0
        self.board_resolution = 1024
        self.sampling_time = 500
        self.serial_arduino = None
        
    
    def on_button_start(self,event):
        if(self.serial_arduino != None):
            self.serial_arduino.close()
        self.btn_start.Hide()
        self.btn_stop.Show()
        self.btn_save_data.Hide()
        self.n=0
        self.time=0
        self.x=np.array([])
        self.y=np.array([])
        take_data=False
        self.serial_connection=False
        self.values = []
        self.stop_acquisition = False
        port_val = self.comm_port.GetSelection()
        port_selected = ""
        if(port_val==-1):
            take_data = False
            wx.CallLater(100,self.show_msg_port())
        else:
            port_selected=self.comm_port.GetString(port_val)
            take_data = True

        if(self.serial_connection == False and take_data==True):
            try:
                self.serial_arduino = serial.Serial(str(port_selected),9600,timeout=1)
                time.sleep(1)
                self.serial_arduino.reset_input_buffer()#Revisar
                self.serial_connection = True
            except:
                self.serial_connection=False
                wx.CallLater(50,self.show_msg_connection())
        if(take_data==True and self.serial_connection==True):
            self.timer.Start(self.sampling_time)

    def show_msg_port(self):
        wx.MessageBox('No COM Port Selected','Serial Communication',
        wx.OK|wx.ICON_ERROR)
    def show_msg_connection(self):
        wx.MessageBox('Failed communication wuth the board',
                      'Communication Error',
                       wx.OK|wx.ICON_ERROR)
    def time_interval(self,event):
        self.btn_stop.Show()
        self.btn_start.Hide()
        self.btn_save_data.Hide()
        if(self.serial_connection ==True):
            sample_size = int(self.spin_ctrl_samples.GetValue())
            try:
                temp = str(self.serial_arduino.readline().decode('cp437'))
                temp = temp.replace("\r\n","")
                value=(float(temp)*(self.high_value_board/self.board_resolution))
                print_console = "Time "+ str(self.time) +" (s)" + "\t"
                print_console += "Voltage " + "{0:.3f}".format(value) + " (V)"
                print(print_console)
                self.values.append(str(self.time+","+str(value)))
                self.x=np.append(self.x,self.time)
                self.y=np.append(self.y,value)
                self.graph.draw(self.x,self.y)
            except:
                pass
            self.time = self.time + 0.5
            self.n = self.n+1
            if(self.n>=sample_size or self.stop_acquisition==True):
                print()
                self.btn_stop.Hide()
                self.btn_start.Show()
                self.btn_save_data.Show()
                self.timer.Stop()
                self.serial_connection = False

    def on_button_stop(self,event):
        self.btn_stop.Hide()
        self.stop_acquisition = True

    def serial_ports(self) -> list:
        if(sys.platform.startswith("win")):
            ports=["COM%s" % (i+1) for i in range(256)]
        elif(sys.platform.startswith("linux") or sys.platform.startswith("cygwin")):
            ports=glob.glob("/dev/tty[A-Za-z]*")
        elif(sys.platform.startswith("darwin")):
            ports=glob.glob("/dev/tty.*")
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            try:
                s=serial.Serial(port)
                s.close()
                result.append(port)

            except(OSError,serial.SerialException):
                pass
            return result


        
    def on_button_save(self,event):
        fdlg = wx.FileDialog(self,"Input setting file path","","","CSV files(*.csv)|*.*",wx.FD_SAVE)
        if(fdlg.ShowModal()==wx.ID_OK):
            self.save_path = fdlg.GetPath()+".csv"
        try:
            myFile= open(self.save_path,"w")
            myFile.write("Time_(s),Voltage_(V)"+"\n")
            for i in range(len(self.values)):
                myFile.write(self.values[i]+"\n")
            myFile.close()
        except:
            pass


class Main(wx.Frame):
    def __init__(self):
        super().__init__(None, title = "SPM with Arduino and wxPython", size=(650,650))
        splitter = wx.SplitterWindow(self)
        top = TopPanel(splitter)
        bottom = BottomPanel(splitter,top)
        splitter.SplitHorizontally(top, bottom, sashPosition = -100)
        splitter.SetMinimumPaneSize(450)
    def OnClose(self,event):
        if (self.serial_arduino != None):
            try:
                self.serial_arduino.close()
            except:
                pass
        self.Destroy()
        
if (__name__=="__main__"):
    app = wx.App(redirect=False)
    frame = Main()
    frame.Show()
    app.MainLoop()