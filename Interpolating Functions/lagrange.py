import math
import matplotlib.pyplot as plt
import numpy as np


def function(x):
    '''''
    Обчислюємо значення даної функції
    '''''
    return x - math.log(2 + math.exp(x) + 2 * math.sqrt(math.exp(2 * x) + math.exp(x) + 1))


def Lagrange(x, y, t):
    '''''
    x, y - масиви вузлів та значень функції в них
    Будуємо поліном Лагранжа L та повертаємо L(t)
    '''''
    z = 0
    for j in range(len(y)):
        a = 1
        b = 1
        for i in range(len(x)):
            if i != j:
                a = a * (t - x[i])
                b = b * (x[j] - x[i])
        z = z + y[j] * a / b
    return z

if __name__ == '__main__':
    # задаємо вузли
    x = np.array([-5,-2,1,4], dtype=float)
    y = np.array([function(i) for i in x])

    print(y, '-значення функції у вузлах')
    print(np.array([Lagrange(x, y, i) for i in x]), '-значення поліному у вузлах')

    # порівнюємо значення в невузлових точках
    points = np.array([-1, 0, 3, 10])
    print(f'Значення в невузлових точках {points} функції:')
    print(np.array([function(i) for i in points]))
    print('Значення в цих точках за поліномом Лагранжа:')
    print(np.array([Lagrange(x, y, i) for i in points]))

    # будуємо графіки поліному Лагранжа та даної функції
    xnew = np.linspace(np.min(x)-10, np.max(x)+10, 100)
    ynew = [Lagrange(x, y, i) for i in xnew]
    #зображуємо вузли на графіку
    plt.plot(x, y, 'o')

    plt.plot(xnew, ynew, label="поліном Лагранжа")
    plt.plot(xnew, [function(i) for i in xnew], label="дана функція")

    # легенда та підписи осей
    plt.legend(loc=0)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()
