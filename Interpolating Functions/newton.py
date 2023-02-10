import math
import matplotlib.pyplot as plt
import numpy as np


def function(x):
    '''''
    Обчислюємо значення даної функції
    '''''
    return x - math.log(2 + math.exp(x) + 2 * math.sqrt(math.exp(2 * x) + math.exp(x) + 1))

def diffenences_array(y):
    '''''
    Обчислюємо скінченні різниці для 4 вузлів
    '''''
    d = []
    y0 = [y[1]-y[0], y[2]-y[1], y[3]-y[2]]
    d.append(y0)
    y1 = [y0[1] - y0[0], y0[2] - y0[1]]
    d.append(y1)
    y2 = [y1[1] - y1[0]]
    d.append(y2)
    return d

def Newton_first(d, h, x, y, t, if_print_coefs):
    '''''
    d - 2D масив скінченних різниць для y
    h - крок сітки
    x, y - масиви вузлів та значень функції в них
    if_print_coefs - змінна bool
    Будуємо перший інтерполяційний поліном Ньютона, виводимо його вигляд (знаходимо коефіцієнти)
    Повертаємо його значення в точці t
    '''''
    coefs_arr = np.array([
        [0, 0, 0, y[0]],
        [0, 0, d[0][0] / h, -x[0] * d[0][0] / h],
        [0, d[1][0] / (2 * h**2), (-x[0] - x[1]) * d[1][0] / (2 * h**2), (x[0] * x[1]) * d[1][0] / (2 * h**2)],
        [d[2][0] / (6 * h**3), (-x[0] - x[1] - x[2]) * d[2][0] / (6 * h**3),
         (x[0] * x[1] + x[1] * x[2] + x[0] * x[2]) * d[2][0] / (6 * h**3), d[2][0] * (-x[0] * x[1] * x[2]) / (6 * h**3)]
    ])
    C = [np.sum(coefs_arr[:, 0]),
         np.sum(coefs_arr[:, 1]),
         np.sum(coefs_arr[:, 2]),
         np.sum(coefs_arr[:, 3])]

    if if_print_coefs == 1:
        print(f'Отриманий інтерполяційний поліном Ньютона:\n{C[0]}x^3 + {C[1]}x^2 + {C[2]}x + {C[3]}')
    return C[0] * t ** 3 + C[1] * t ** 2 + C[2] * t + C[3]

def Newton_second(d, h, x, y, t):
    '''''
    d - 2D масив скінченних різниць для y
    h - крок сітки
    x, y - масиви вузлів та значень функції в них
    Будуємо другий інтерполяційний поліном Ньютона P та повертаємо P(t)
    '''''
    n = len(x)
    z = y[-1]
    for j in range(n):
        a = 1
        for i in range(j):
            a = a * (t - x[n-i-1])
        if j!=0:
            z = z + d[j-1][-1] * a / math.factorial(j)/(h**j)
    return z

if __name__ == '__main__':
    # задаємо вузли
    x = np.array([-5,-2,1,4], dtype=float)
    y = np.array([function(i) for i in x])


    # масив скінченних різниць
    d = diffenences_array(y)
    print('Масив скінченних різниць:\n', d)

    # виводимо поліном
    print(Newton_first(d, 3, x, y, x[0], 1), '- значення у базовому вузлі функції')

    # порівнюємо значення в невузлових точках
    points = np.array([-7, -6, 0, 5, 10])
    print(f'Значення в невузлових точках {points} функції:')
    print(np.array([function(i) for i in points]))
    print('Значення в цих точках за 1м поліномом Ньютона:')
    print(np.array([Newton_first(d, 3, x, y, i, 0) for i in points]))
    print('Значення в цих точках за 2м поліномом Ньютона:')
    print(np.array([Newton_second(d, 3, x, y, i) for i in points]))


    xnew = np.linspace(np.min(x)-10, np.max(x)+10, 100)
    polin1 = [Newton_first(d, 3, x, y, i, 0) for i in xnew]
    polin2 = [Newton_second(d, 3, x, y, i) for i in xnew]

    # будуємо графіки 1 поліному Ньютона та даної функції
    plt.plot(xnew, polin1, label="1й поліном Ньютона")
    #зображуємо вузли на графіку
    plt.plot(x, y, 'o')
    plt.plot(xnew, [function(i) for i in xnew], label="дана функція")

    # легенда та підписи осей
    plt.legend(loc=0)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()

    # будуємо графіки 2 поліному Ньютона та даної функції
    plt.plot(xnew, polin2, label="2й поліном Ньютона")
    plt.plot(xnew, [function(i) for i in xnew], label="дана функція")
    # зображуємо вузли на графіку
    plt.plot(x, y, 'o')

    # легенда та підписи осей
    plt.legend(loc=0)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()
