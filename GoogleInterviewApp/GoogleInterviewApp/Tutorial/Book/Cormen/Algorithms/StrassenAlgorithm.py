import numpy as np

def add_matrix(a,b):
    return np.add(a,b)

def substract_matrix(a,b):
    return np.subtract(a,b)

def strassen(matrixA, matrixB):
    n = len(matrixA)
    
    if n == 1:
        matrixA * matrixB

    mid = n // 2

    a11 = matrixA[:mid,:mid]
    a12 = matrixA[:mid, mid:]
    a21 = matrixA[mid:, :mid]
    a22 = matrixA[mid:, mid:]
    
    b11 = matrixB[:mid, :mid]
    b12 = matrixB[:mid, mid:]
    b21 = matrixB[mid:, :mid]
    b22 = matrixB[mid:, mid:]
    
    m1 = strassen(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen(add_matrix(a11, a22), b11)
    m3 = strassen(a11, substract_matrix(b12, b22))
    m4 = strassen(a22, substract_matrix(b21, b11))
    m5 = strassen(add_matrix(a11, a12), b22)
    m6 = strassen(substract_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen(substract_matrix(a12, a22), add_matrix(b11, b22))

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6
    
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c

X = np.array([[12,7,3], [4 ,5,6], [7 ,8,9]])

Y = np.array([[5,8,1,2], [6,7,3,0], [4,5,9,1]])

print(strassen(X, Y))