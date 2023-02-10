#заданий алгебричний многочлен
def my_func(x):
    return 55*x**7-336*x**6+297*x**5+869*x**4-823*x**3-561*x**2+63*x+23

#функція, що повертає список інтервалів
def array_of_sections():
    arr = []
    k = -3.5
    while k<5:
        if my_func(k)*my_func(k+0.1)<0:
            arr.append([k, k+0.1])
        k+=0.1
    return arr

def bisection(section, func, eps):
    a, b = section[0], section[1]
    c = 0.5*(a+b)
    fc = func(c)
    print("Кінці інтервалу [a,b]:", section)
    print("Значення функції на кінцях інтервалу:", [func(a), func(b)])
    if (b-a) < eps or abs(fc) < eps:
        print("Шуканий корінь на відрізку:")
        return c
    if func(a)*func(c) < 0:
        return bisection([a, c], func, eps)
    else:
        return bisection([c, b], func, eps)

for i in range(7):
    print(bisection(array_of_sections()[i], my_func, 0.00001))

