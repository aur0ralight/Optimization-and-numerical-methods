def my_func(x):
    return 55*x**7-336*x**6+297*x**5+869*x**4-823*x**3-561*x**2+63*x+23

def sec_derivative(x):
    return 6*(-187 - 823*x + 1738*x**2 + 990*x**3 - 1680*x**4 + 385*x**5)

#функція, що повертає список інтервалів
def array_of_sections():
    arr = []
    k = -3.5
    while k<5:
        if my_func(k)*my_func(k+0.1)<0:
            arr.append([k, k+0.1])
        k+=0.1
    return arr

def secant(section, sec_deriv, func, eps):
    a, b = section[0], section[1]
    if sec_deriv(0.5 * (a + b)) * func(a) > 0:
        x = b
        while 1:
            x_k = x
            x = x-(func(x)*(x-a))/(func(x)-func(a))
            print("Кінці інтервалу:", [a, x_k])
            print("Значення функції на кінцях інтервалу:", [func(a), func(x_k)])
            if abs(x-x_k) < eps or abs(func(x)) < eps:
                print("Кінці інтервалу:", [a, x])
                print("Значення функції на кінцях інтервалу:", [func(a), func(x)])
                print("Шуканий корінь:")
                return x
    else:
        x = a
        while 1:
            x_k = x
            x = x - (func(x) * (b - x)) / (func(b) - func(x))
            print("Кінці інтервалу:", [x_k, b])
            print("Значення функції на кінцях інтервалу:", [func(x_k), func(b)])
            if abs(x - x_k) < eps or abs(func(x)) < eps:
                print("Кінці інтервалу:", [x, b])
                print("Значення функції на кінцях інтервалу:", [func(x), func(b)])
                print("Шуканий корінь:")
                return x

for i in range(7):
    print(secant(array_of_sections()[i],sec_derivative, my_func, 0.00001))
