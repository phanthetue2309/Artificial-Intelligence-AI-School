import numpy as np

def matrix_factorization(matrix, beta, K, stopping_condition):
    m = np.shape(matrix)[0]
    n = np.shape(matrix)[1]
    matrix_W = np.random.normal(0,1,m+K).reshape((m,K))
    matrix_H = np.random.normal(0,1,K+n).reshape((K,n))
    counter = 0

    while( counter < stopping_condition) : 
        for u in range(m) :
            for i in range(n):
                if (matrix[u][i] > 0) :
                    r = 0 
                    for k in range(len(matrix)) : 
                        r += matrix_W[u][k] * matrix_H[i][k]
                    e = matrix[u][i] - r

                    for k in range(len(matrix)) : 
                        matrix_W[u][k] += beta * e * matrix_H[i][k]
                        matrix_H[i][k] += beta * e * matrix_W[u][k]
        counter += 1
    return matrix_W, matrix_H


