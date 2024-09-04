def brute_force(x, y):
    # result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [[0 for x in range(len(x))] for y in range(len(y[0]))]
    
    for i in range(0, len(x)):
        for j in range(0, len(y[0])):
            for k in range(0, len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result



X = [[3,5,1,3],
     [1,2,3,4],
     [4,5,6,8],
     [7,8,9,3]]
 
Y = [[4,1,2,3],
     [1,2,1,6],
     [2,4,6,2],
     [6,2,5,4]]

print(brute_force(X, Y))