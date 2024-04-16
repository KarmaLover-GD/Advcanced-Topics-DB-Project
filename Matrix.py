import numpy as np
import time
from collections import defaultdict
from multiprocessing import Pool
from functools import reduce
#  part a) matrix multiplication without map reduce.

val = 3000

def create_matrix(x, y):
    mat = np.random.randint(0, 100, (x, y))

    return mat

def multiply_matrix(A, B):
    return np.matmul(A, B)

A = create_matrix(val, val) 
B = create_matrix(val, val)
start = time.time()
multiply_matrix(A, B)
end = time.time() 
print("\nTime Taken for normal computaiton" , end- start )

start = time.time()




def matrix_multiply_MR(matrix1, matrix2):
    chunk_size = 100
    chunks_matrix1 = [matrix1[i:i+chunk_size] for i in range(0, len(matrix1), chunk_size)]
    chunks_matrix2 = [matrix2[:, i:i+chunk_size] for i in range(0, len(matrix2), chunk_size)]

# Initialize the result matrix
    result_matrix = np.zeros((len(matrix1[0]), len(matrix1[0])))

# Perform Map and Reduce
    for i, chunk_row in enumerate(chunks_matrix1):
        for j, chunk_col in enumerate(chunks_matrix2):
            # Compute the multiplication of the current chunk
            chunk_result = np.dot(chunk_row, chunk_col)
            # Update the corresponding part of the result matrix
            result_matrix[i*chunk_size:(i+1)*chunk_size, j*chunk_size:(j+1)*chunk_size] = chunk_result
    
    return result_matrix

result_matrix = matrix_multiply_MR(A, B)
end = time.time()

print("\nTime Taken for computaiton Map reduce" , end- start )




    
