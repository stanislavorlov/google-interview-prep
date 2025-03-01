def square_matrix_multiply(matrix_a, matrix_b):
    n = len(matrix_a)
    matrix_c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result = 0
            for k in range(n):
                result += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = result

    return matrix_c

def square_matrix_multiply_recursive(matrix_a, matrix_b):
    n = len(matrix_a)
    matrix_c = [[0 for _ in range(n)] for _ in range(n)]

    def multiply(m_a, m_b, m_c, i, j, k):
        if i >= len(m_a):
            return
        if j >= len(m_b[0]):
            return multiply(m_a, m_b, m_c, i+1,0,0)
        if k >= len(m_b):
            return multiply(m_a, m_b, m_c, i, j+1, 0)
        m_c[i][j] += m_a[i][k] * m_b[k][j]
        multiply(m_a, m_b, m_c, i, j, k+1)

    multiply(matrix_a, matrix_b, matrix_c, 0, 0, 0)

    return matrix_c

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = square_matrix_multiply(a,b)
d = square_matrix_multiply_recursive(a,b)
print(c)
print(d)