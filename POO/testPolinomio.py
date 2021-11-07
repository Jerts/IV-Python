from Polinomio import Polynomial

p1 = Polynomial([1,-1,])
p2 = Polynomial([0,1,0,0,-6,-1])
print("Polinomio p1: ",p1(2))
p3=p2+p1
print("Polinomio p3 = pq + p2 =", p3)
print("Coeficientes p3 =",p3.coeff)
p4=p1*p2
print("Polinomio p4 = p1 * p2 =", p4)
p5 = p2.derivative()
print("dp2/dx",p5)
x=1
print("p2(x=%g) = %g" %(x,p2(x)))
