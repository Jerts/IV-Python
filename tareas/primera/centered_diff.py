import math

def diff(f,x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

def test_diff(f,x,h,expected):
    test = diff(f,x,h)
    print(f'Expected value: {expected}, returned by diff(): {test}, error = {expected-test}')

if __name__ == '__main__':
    test_diff(lambda x: math.exp(x),0,0.01,1)
    test_diff(lambda x: math.exp(-2*x**2),0,0.01,0)
    test_diff(lambda x: math.cos(x),2*math.pi,0.01,0)
    test_diff(lambda x: math.log(x),1,0.01,1)
    