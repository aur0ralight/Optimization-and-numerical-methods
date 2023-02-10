import numpy as np
import pandas as pd
import math

def system(x):
    #повертає значення x_(k+1) на новій ітерації
    return np.array([0.5*(2-math.cos(x[1])),
                     math.sin(x[0] + 1) - 1.2])
def F(x):
    #повертає значення системи в заданому наближенні
    return np.array([math.sin(x[0] + 1) - 1.2 - x[1],
                     2*x[0] + math.cos(x[1]) - 2])

def norm(X):
    # обчислює норму як максимальну суму модулів по рядках
    sums = []
    for i in range(X.shape[0]):
        sums.append(np.sum(np.absolute(X[i])))
    return max(sums)

def fixed_point_iteration(x, sys, eps):
    #метод простих ітерацій
    table = pd.DataFrame([np.concatenate((x, np.array([None])))], columns=['x', 'y', '\u0394'])
    i = 1
    while(True):
        x_new = sys(x)
        #додаємо на новій ітерації відповідний вектор
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

x_0 = np.array([0.5, -0.2])
#x_0 = np.array([0, 0])
x = fixed_point_iteration(x_0, system, 0.00001)
