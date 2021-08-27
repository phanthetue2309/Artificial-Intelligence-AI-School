import numpy as np


def f(x):
    return (np.exp(x) - 2 / np.exp(x))**2


def grad(x):
    return 2*(np.exp(x) - (2 / np.exp(x))) * (np.exp(x) + (2 / np.exp(2*x)))


def gradientDescent(x, n):
    x = [x]
    for i in range(1000):
        x_new = x[-1] - n * grad(x[-1])
        if abs(grad(x_new)) < 0.0001:
            break
        x.append(x_new)
    return (x[-1], i)


if __name__ == "__main__":
    (x, i) = gradientDescent(-1, 0.1)
    print("x = %f\t i = %d" % (x, i))
    print("f = %f" % (f(x)))

    (x, i) = gradientDescent(1, 0.1)
    print("x = %f\t i = %d" % (x, i))
    print("f = %f" % (f(x)))
