
from __future__ import division
import random
import time
import numpy as np

class NN():
    def __init__(self, layers):
       
        self.layers = layers
        self.L = len(layers)  
        self.w = [np.random.randn(l2, l1 + 1) for l2, l1 in zip(layers[1:], layers[:-1])]
        
    def train(self, train_data, epochs, mini_batch_size, eta):
    
        # number of training data        
        m = len(train_data)
        # cost
        cost = []
        for j in range(epochs):
            start_time = time.time()
            print('Epoch {0} begin...'.format(j + 1))
            # shuffle data before run
            random.shuffle(train_data)
            # divide data into mini batchs
            for k in range(0, m, mini_batch_size):
                mini_batch = train_data[k:k+mini_batch_size]
                m_batch = len(mini_batch)
                # calc gradient
                w_grad = [np.zeros(W.shape) for W in self.w]
                for x, y in mini_batch:
                    grad = self.backprop(x, y)
                    w_grad = [W_grad + g for W_grad, g in zip(w_grad, grad)]
                w_grad = [W_grad / m_batch for W_grad in w_grad]
                
                # check grad for first mini_batch in first epoch
                if j == 0  and k == 0 and not self.check_grad(mini_batch, w_grad):
                    print('backprop fail!')
                    return False
                
                # update w
                self.w = [W - eta * W_grad for W, W_grad in zip(self.w, w_grad)]
            
            # calc cost
            cost.append(self.cost(train_data))
            print('Epoch {0} done: {1}'.format(j + 1, time.time() - start_time))
            
        return cost
    
    def predict(self, x):

        _, a = self.feedforward(x)
        return np.argmax(a[-1])
    
    def evaluate(self, test_data):
        results = [(self.predict(x), y) for (x, y) in test_data]
        return sum(int(_y == y) for (_y, y) in results)
    
    def feedforward(self, x):
      
        z = []
        a = [self.add_bias(x)]
        for l in range(1, self.L):
            z_l = np.dot(self.w[l-1], a[l-1])
            a_l = self.sigmoid(z_l)
            if l < self.L - 1:
                a_l = self.add_bias(a_l)
            
            z.append(z_l)
            a.append(a_l)
            
        return (z, a)
    
    def backprop(self, x, y):

        w_grad = [np.zeros(W.shape) for W in self.w]
        # feedforward
        z, a = self.feedforward(x)
        # backward
        dz = a[-1] - y
        for _l in range(1, self.L):
            l = -_l # layer index
            if l < -1:
                da = self.sigmoid_grad(z[l])
                # do not calc for w_0 (da_0 / dz = 0 because of a_0 = 1 for all z)
                dz = np.dot(self.w[l+1][:, 1:].transpose(), dz) * da
            # gradient    
            w_grad[l] = np.dot(dz, a[l-1].transpose())
        
        return w_grad
    
    def add_bias(self, a):

        return np.insert(a, 0, 1, axis=0)
    
    def check_grad(self, data, grad, epsilon=1e-4, threshold=1e-6):

        for l in range(self.L - 1):
            n_row, n_col = self.w[l].shape
            for i in range(n_row):
                for j in range(n_col):
                    w_l_ij = self.w[l][i][j]
                    # left
                    self.w[l][i][j] = w_l_ij - epsilon
                    l_cost = self.cost(data)
                    # right
                    self.w[l][i][j] = w_l_ij + epsilon
                    r_cost = self.cost(data)
                    # numerical grad
                    num_grad = (r_cost - l_cost) / (2 * epsilon)
                    
                    # diff
                    diff = abs(grad[l][i][j] - num_grad)
                    
                    # reset w
                    self.w[l][i][j] = w_l_ij
                    
                    if diff > threshold:
                        print('Check Grad Error at (l: {0}, col: {1}, row: {2}), | num_grad: {3} vs backprop grad: {4} | : {5}'
                              .format(l, i, j, num_grad, grad[l][i][j], diff))
                        return False
        
        return True
    
    def cost(self, data):

        m = len(data)
        j = 0
        for x, y in data:
            _, a = self.feedforward(x)
            a_L = a[-1]
            j += np.sum(np.nan_to_num(y*np.log(a_L) + (1-y)*np.log(1-a_L)))
        return -j / m
    
    def sigmoid(self, z):

        return 1.0 / (1.0 + np.exp(-z))
    
    def sigmoid_grad(self, z):

        s = self.sigmoid(z)
        return s * (1 - s)

