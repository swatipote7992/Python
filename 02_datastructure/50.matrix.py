matrix = [
    [1,2,3],
    [4,5,6]
]

# matrix traversal
# put elements vertically
print('matrix_traversal')
def matrix_traversal(matrix):
    for row in matrix:
        for col in row:
            print(col)

matrix_traversal(matrix)

#Sum of All Matrix Elements
def sum_all(matrix):
    result = 0
    for row in matrix:
        for col in row:
            result += col
    return result

print('sum_all:', sum_all(matrix))

#Given a matrix, calculate the sum of each row.
def row_sum(matrix):
    result=[]
    for row in matrix:
        rowTotal = 0
        for col in row:
            rowTotal += col
        result.append(rowTotal)
    return result

print('row_sum;', row_sum(matrix))

#Given a matrix, calculate the sum of each column.
def col_sum(matrix):
    result=[]
    row_len = len(matrix)
    col_len = len(matrix[0])
    for col in range(col_len):
        col_total = 0
        for row in range(row_len):
            col_total += matrix[row][col]
        result.append(col_total)
    return result

print("col_sum:", col_sum(matrix))


# Transpose Matrix
# Given a matrix, return its transpose. The rows become columns and the columns become rows.
def transpose_matrix(matrix):
    result=[]
    row_len = len(matrix)
    col_len = len(matrix[0])
    for col in range(col_len):
        result_row = []
        for row in range(row_len):
            result_row.append(matrix[row][col])
        result.append(result_row)
    return result

print('transpose_matrix:', transpose_matrix(matrix))

# Matrix Multiplication
# Given two matrices A and B, multiply them and return the resulting matrix.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

rows_a = len(A)
cols_a = len(A[0])
rows_b = len(B)
cols_b = len(B[0])

# create result matrix
result_mulmat = [[0] * cols_b for _ in range(rows_a)]
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result_mulmat[i][j] += A[i][k] * B[k][j]

print('result_mulmat', result_mulmat)

