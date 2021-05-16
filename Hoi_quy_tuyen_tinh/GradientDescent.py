import numpy as np
def grad(x):
    return 2*x + 5*np.cos(x)
def f(x):
    return x**2 + 5*np.sin(x)
def gradientDescent(x,n):
    x = [x]
    for i in range(100):
        x_new = x[-1] - n*grad(x[-1])
        if abs(grad(x_new)) < 0.0001:
            break
        x.append(x_new)
    return (x[-1], i)

if __name__ == '__main__':
    (x,i) = gradientDescent(-5, 0.1)
    print("x = %f\t i = %d" %(x, i))
    print("f = %f" %(f(x)))
    (x, i) = gradientDescent(5, 0.1)
    print("x = %f\t i = %d" % (x, i))
    print("f = %f" % (f(x)))