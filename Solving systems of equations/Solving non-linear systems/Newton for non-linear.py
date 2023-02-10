import numpy as np
import pandas as pd
import math

def W(x):
    # повертає значення матриці Якобі в заданій точці
    return np.array([[x[1]/((math.cos(x[0]*x[1]+0.4))**2) - 2*x[0], x[0]/((math.cos(x[0]*x[1]+0.4))**2)],
                     [1.2*x[0], 4*x[1]]])

def F(x):
    # повертає значення системи в заданій точці
    return np.array([math.tan(x[0]*x[1]+0.4) - x[0]**2,
                     0.6*x[0]**2 + 2*x[1]**2 - 1])

def norm(X):
    # обчислює норму як максимальну суму модулів по рядках
    sums = []
    for i in range(X.shape[0]):
        sums.append(np.sum(np.absolute(X[i])))
    return max(sums)

def Newton(x, W, F, eps):
    table = pd.DataFrame([np.concatenate((x, np.array([None])))], columns=['x', 'y', '\u0394'])
    i = 1
    while (True):
        #реалізація ітераційної формули
        delta_x = np.linalg.solve(W(x), (-1)*F(x))
        x_new = x + delta_x
        # додаємо на новій ітерації відповідний вектор
        table.loc[i] = np.concatenate((x_new, np.array([norm(x_new - x)])))
        if (norm(x_new - x) < eps):
            x = x_new
            break
        i += 1
        x = x_new
    print(table)
    print("Підставимо отриманий наближений розв'язок в систему:")
    print("F(x_*) = ", F(x))
    return x

x_0 = np.array([1, 0.5])
#x_0 = np.array([2, 2])
x = Newton(x_0, W, F, 0.00001)

