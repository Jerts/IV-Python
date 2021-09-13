from _typeshed import Self


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