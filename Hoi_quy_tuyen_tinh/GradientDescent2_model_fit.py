import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# method use lib sklearn


def UserLR(X, y):
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y.reshape(-1, 1))
    (w, b) = (model.coef_[0][0], model.intercept_[0])
    #sol_skl = np.array([w, b])
    return (w, b)


if __name__ == '__main__':
    # data
    X = np.random.rand(100)
    y = 4 + 3 * X + .5 * np.random.rand(100)  # add noise
    # -----------------
    (w, b) = UserLR(X, y)
    print("w = %f\t b = %f" % (w, b))
    plt.plot(X.T, y.T, 'b.')
    # ------------------
    x0 = np.linspace(0, 1, 2, endpoint=True)
    y0 = w * x0 + b
    plt.plot(x0, y0, 'y', linewidth=4)
    plt.axis([0, 1, 0, 10])
    plt.show()
    # ---------
