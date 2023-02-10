import numpy as np
import pandas as pd

A = np.array([[4.003, 0.207, 0.519, 0.281],
             [0.416, 3.273, 0.326, 0.375],
             [0.297, 0.351, 2.997, 0.429],
             [0.412, 0.194, 0.215, 3.628]])
b = np.array([0.425, 0.021, 0.213, 0.946])

def norm(X):
    # calculates norm as max of sum of modules in rows
    sums = []
    for i in range(X.shape[0]):
            sums.append(np.sum(np.absolute(X[i])))
    return max(sums)

def lovely_Jacobi(matrix, vect, x0_is_c, eps):
    n = matrix.shape[0]
    if n!= matrix.shape[1]:
        return "Oops! Not a n*n input matrix"
    # initializing matrices we`ll use and filling them
    L, D_rev, R = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            L[i, j] = matrix[i, j]
    for i in range(n):
        D_rev[i, i] = 1/matrix[i, i]
    for i in range(n):
        for j in range(i+1, n):
            R[i, j] = matrix[i, j]

    B = -D_rev@(L+R)
    print("Norm of matrix B:")
    print(norm(B))
    c = D_rev@vect
    # setting the initial approximation according to the bool parameter
    x = np.array([1,1,1,1])
    if x0_is_c:
        x = c
    table = pd.DataFrame([np.concatenate((x,np.array([None])))], columns=['x1','x2','x3','x4','||x(k)-x(k-1)||'])

    print("Table of approximations is:")
    # iteration loop
    i=1
    while(True):
        x_new = B@x+c
        table.loc[i] = np.concatenate((x_new, np.array([norm(x_new - x)])))
        if(norm(x_new - x)<eps):
            x = x_new
            break
        i+=1
        x = x_new

    print(table)

    #обчислення і вивід вектору нев'язки
    print("\nResidual vector (with values, close to 0):")
    res_vector = vect - matrix@x
    print(res_vector)

    print(f"\nThe desired solution (x1,...,x{n}) is:")
    return np.round(x, 5)


print("Method with initial approximation x_0=c")
# print(lovely_Jacobi(A, b, 1, 0.00001))
# print("\n\n")
print("Method with initial approximation x_0=(0,0,0,0)")
print(lovely_Jacobi(A, b, 0, 0.00001))