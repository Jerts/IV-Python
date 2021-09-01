from pathlength import pathlength
import math as m

def get_circle_points(n):
    x=[(1/2)*m.cos((2*m.pi*i)/n) for i in range(0,n+1)]
    y=[(1/2)*m.sin((2*m.pi*i)/n) for i in range(0,n+1)]
    return x,y

if __name__=="__main__":
    k=5
    n=2**k
    print(f'N es {n}')
    x,y = get_circle_points(n)
    pi_estimate = pathlength(x,y)
    print(f'Error de aproximacion de pi: {m.pi-pi_estimate}')