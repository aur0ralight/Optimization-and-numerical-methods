def my_func(x):
    # Use a breakpoint in the code line below to debug your script.
    return 55*x**7-336*x**6+297*x**5+869*x**4-823*x**3-561*x**2+63*x+23

def derivative(x):
    # Use a breakpoint in the code line below to debug your script.
    return 63 - 1122*x - 2469*x**2 + 3476*x**3 + 1485*x**4 - 2016*x**5 + 385*x**6

def sec_derivative(x):
    # Use a breakpoint in the code line below to debug your script.
    return 6*(-187 - 823*x + 1738*x**2 + 990*x**3 - 1680*x**4 + 385*x**5)

def array_of_sections():
    arr = []
    k = -3.5
    while k<5:
        if my_func(k)*my_func(k+0.1)<0:
            arr.append([k, k+0.1])
        k+=0.1
    return arr
print(array_of_sections())