import numpy as np

A = np.array([[4.4, -2.5, 19.2, -10.8],
              [5.5, -9.3, -14.2, 13.2],
              [7.1, -11.5, 5.3, -6.7],
              [14.2, 23.4, -8.8, 5.3]])
v_b = np.array([4.3, 6.8, -1.8, 7.2])

def determinant_of_triang_matrix(A):
    return np.prod([A[i, i] for i in range(0, A.shape[0])])

def max_element_incolumn(matrix_a, vector_b, k):
    ind = k + np.argmax(np.abs(matrix_a[k:, k]))
    if ind != k:
        matrix_a[k, :], matrix_a[ind, :] = np.copy(matrix_a[ind, :]), np.copy(matrix_a[k, :])
        vector_b[k], vector_b[ind] = np.copy(vector_b[ind]), np.copy(vector_b[k])

def DearGauss(matrix_a, vector_b):
    a = np.copy(matrix_a)
    b = np.copy(vector_b)
    print('Given matrix and vector of coefs:\n', a,"\nb:", b)

    # прямий хід хід метода Гаусса з постовпчиковим вибором головного елементу
    for k in range(0, a.shape[0]):
        max_element_incolumn(a, b, k)
        for i in range(k+1, a.shape[0]):
            elem = a[i, k]
            for j in range(k, a.shape[1]):
                a[i, j] -= elem * a[k, j] / a[k, k]
            b[i] -= elem*b[k]/a[k, k]
        print(f"Matrix on {k+1} step and vector of coefs:\n", a,"\nb:", b)


    #на цьому кроці матриця А трикутна, обчислюємо її визначник
    print("\nDeterminant of the matrix:\n", determinant_of_triang_matrix(a))

    #зворотнiй хід метода Гаусса
    x = np.zeros((a.shape[0]))
    for k in range(a.shape[0]-1, -1, -1):
        sum_ax = 0
        for j in range(k+1, a.shape[0]):
            sum_ax += a[k, j]*x[j]
        x[k] = (b[k] - sum_ax)/a[k, k]

    #округлення результату до 10 знаків після коми
    x = x.round(5)

    #обчислення і вивід вектору нев'язки
    print("\nResidual vector (with values, close to 0):")
    res_vector = vector_b - matrix_a@x
    print(res_vector)

    #вивід отриманих коренів СЛАР від х_0 до х_n (відповідь)
    print(f"\nResult vector of {a.shape[0]} solutions:")
    return x

print(DearGauss(A, v_b))