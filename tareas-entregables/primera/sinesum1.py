import math
import matplotlib.pyplot as plt
import numpy as np

def S(time,n_iter,T):
    aux_list=[]
    aux_acc= 0
    for t in time:
        for i in n_iter:
            aux_acc += (1/(2*i - 1))*math.sin((2*(2*i-1)*math.pi*t)/T)
            print(aux_acc)
        aux_list.append((4/math.pi)*aux_acc)
        aux_acc = 0
    return aux_list    

def f(t,T):
    aux_list = []
    for p in t:
        if p>0 and p<T/2:
            aux_list.append(1)
        elif p==T/2:
            aux_list.append(0)
        elif p>T/2 and p<T:
            aux_list.append(-1)
        else:
            print('t out of range, error on the arguments!!')
    return aux_list

if __name__ == "__main__":
    top=5
    n = range(1,top+1)
    T=2*math.pi
    alpha = np.linspace(0.01,0.99,50)
    t = [ T*e for e in alpha ]
    print(t)
    St = S(t,n,T)
    ft = f(t,T)

    plt.plot(t,St,'g--')
    plt.plot(t,ft,'b.-')
    plt.show()
    print(f'N# |f(t)|S(t)|err|')
    print(f'-------------------------')
    for i in range(0,len(St)):
        print(f'{i}  | {ft[i]} | {St[i]:.3f} | {(ft[i]-St[i]):.3f}')