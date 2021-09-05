def pathlength(x,y):
    acc=0
    for i in range(1,len(x)):
        acc+=(pow(x[i]-x[i-1],2)+pow(y[i]-y[i-1],2))**(0.5)
    return acc
def test_pathlength():
    x=[0,2,6,8]
    y=[0,0,0,0]
    distance = pathlength(x,y)
    expected_result=9
    if(distance==expected_result):
        print(f'Resultado correcto')
        print(f'Valor esperado: {expected_result}, valor regresado: {distance}')
    else:
        print(f'Valor incorrecto regresado: {distance}')

if __name__ == '__main__':
    test_pathlength()