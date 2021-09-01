import math
import numpy as np

def gauss(x, m=0,s=1):
    return (1/(math.sqrt(2*math.pi)*s))*math.pow(math.e,(-1/2)*((x-m)/s)**2)

if __name__ == "__main__":
    m=0
    s=1
    n=60
    points = np.linspace(m-5*s,m+5*s,n)
    x = [gauss(x,m,s) for x in points]
    print(x)