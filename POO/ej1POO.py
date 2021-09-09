class Y:
    def __init__(self,y0,v0):
        self.y0 = y0
        self.v0 = v0
        self.g=9.81

    #Primera forma de evaluar la funcion y=y0+v0*t+0.5*g*t^2
    def value(self,t):
        return self.y0+self.v0*t+0.5*self.g*t**2

    def __call__(self, t):
        return self.y0+self.v0*t+0.5*self.g*t**2

    def formula(self):
        print("y = %g + %g*t + 0.5*%g*t^2"%(self.y0,self.v0,self.g))

y0 = 10
v0 = 5
#Objeto
objeto_y = Y(y0,v0)
t=0.2
#Evaluar funcion 
y1 = objeto_y.value(t)
y2 = objeto_y(t)
print("Primere llada a la funci[on del m[etodo evaluar",y1)
print("Segunda llamada a la  funcion del metodo call",y2)
objeto_y.formula()