import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Gradient Descent
def rad(w):
    N = Xbar.shape[0]
    return (1/N)*Xbar.T.dot((Xbar.dot(w)) -y)
def L(w):
    N = Xbar.shape[0]
    return 0.5/N*np.linalg.norm(y - Xbar.dot(w))**2
def myGD(w_init, grad, n):
    w = [w_init]
    for i in range(100):
        w_new = w[-1] - n*rad(w[-1])
        if np.linalg.norm(rad(w_new))/len(w_new) < 1e-3:
            break
       # print(w_ne)
        w.append(w_new)
    return (w, i)

def myGD_Momentum(theta_init, grad, lamda, Xema):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)
    for i in range(100):
        v_new = Xema * v_old + lamda * grad(theta[-1])
        theta_new = theta[-1] - v_new
        if np.linalg.norm(grad(theta_new)) / np.array(theta_init).size < 1e-3:
            break
        theta.append(theta_new)
        v_old = v_new
    return (i, theta)

def myGD_NAG(theta_init, grad, lamda, Xema):
    theta = [theta_init]
    v_old = [np.zeros_like(theta_init)]
    for i in range(100):
        v_new = Xema*v_old[-1] + lamda *grad(theta[-1]-Xema*v_old[-1])
        theta_new = theta - v_new
        if np.linalg.norm(grad(theta_new-Xema*v_new)) / np.array(theta_init).size < 1e-3:
            break
        theta.append(theta_new)
        v_old.append(v_new)
    return (i,theta)

if __name__ == '__main__':
    X = np.random.rand(1000)
    y = 4 + 3 * X + .5 * np.random.rand(1000)

    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X.reshape(-1, 1)), axis=1)
    w_init = np.array([[2], [1]])
    (w, i) = myGD(w_init, rad, 1)
    w1 = w[-1].T
    w2 = w1[-1]
    print(w2)