import numpy as np
import time
#  part a) matrix multiplication without map reduce.


def create_matrix(x, y):
    mat = np.random.randint(0, 100, (x, y))

    return mat

def multiply_matrix(A, B, x, y):
    C = np.zeros((x, y))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                print("Position : ", (i, j, k))
                C[i][j] += A[i][k] * B[k][j]
    return C

A = create_matrix(100, 100) 
B = create_matrix(100, 100)
start = time.time()
multiply_matrix(A, B, 100, 100)
end = time.time()
print("\nTime Taken = " , end- start)
    