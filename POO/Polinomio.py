class Polynomial:
    def __init__(self,coeficients) -> None:
        self.coeff = coeficients

    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __add__(self,other):
        if(len(self.coeff))>len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] = result_coeff[i]+ other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] = result_coeff[i]+ self.coeff[i]
        return Polynomial(result_coeff)

    def diferentiate(self):
        for i in range(1,len(self.coeff)):
            self.coeff[i-1] = i * self.coeff[i]
        del self.coeff[-1]
    
    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.diferentiate()
        return dpdx
    
    def __mul__(self,other):
        c = self.coeff
        d = other.coeff
        M = len(c)-1
        N = len(d)-1
        import numpy as np
        result_coeff = np.zeros(M+N+1)
        for i in range(M+1):
            for j in range(N+1):
                result_coeff[i+j] = result_coeff[i+j] + c[i]*d[j]
        return Polynomial(result_coeff)

    def __str__(self):
        s = ""
        for i in range(len(self.coeff)):
            if(self.coeff[i]!=0):
                s += " + %g*x^%d"%(self.coeff[i],i)
            s= s.replace("+ -","- ")
            s=s.replace("x^0","1")
            s=s.replace("1*"," ")
            s=s.replace("x^1","x")
            if(s[0:3]==" + "):
                s=s[3:]
            if(s[0:3]==" - "):
                s = "-" + s[3:]

        return s