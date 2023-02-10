def my_func(x):
    return 55*x**7-336*x**6+297*x**5+869*x**4-823*x**3-561*x**2+63*x+23

def derivative(x):
    return 63 - 1122*x - 2469*x**2 + 3476*x**3 + 1485*x**4 - 2016*x**5 + 385*x**6

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

def newtons(section, deriv, sec_deriv, func, eps):
    a, b = section[0], section[1]
    k = a
    while k<b:
        if sec_deriv(k) * func(k) > 0:
            x = k
        k+=0.0001
    while 1:
        x_k = x
        x = x - (func(x)) / deriv(x)
        print("Поточне наближення та значення функції:", [x_k, func(x_k)])
        if abs(x - x_k) < eps or abs(func(x)) < eps:
            print("Поточне наближення та значення функції:", [x, func(x)])
            print("Шуканий корінь:")
            return x

for i in range(7):
    print(newtons(array_of_sections()[i],derivative,sec_derivative, my_func, 0.00001))