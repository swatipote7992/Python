# Main Diagonal Sum
# Problem Statement

# Given a square matrix, calculate the sum of the elements on the main diagonal.

# Code
# def diagonal_sum(matrix):
#     total = 0

#     for i in range(len(matrix)):
#         total += matrix[i][i]

#     return total


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(diagonal_sum(matrix))
# Output
# 15

# Both Diagonal Sums
# Problem Statement

# Given a square matrix, calculate the sum of both the main and secondary diagonals.

# Code
# def diagonal_sums(matrix):
#     n = len(matrix)

#     main = 0
#     secondary = 0

#     for i in range(n):
#         main += matrix[i][i]
#         secondary += matrix[i][n - 1 - i]

#     return main, secondary


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# main, secondary = diagonal_sums(matrix)

# print("Main:", main)
# print("Secondary:", secondary)
# Output
# Main: 15
# Secondary: 15

# Rotate Matrix 90° Clockwise
# Problem Statement

# Given a square matrix, rotate it 90 degrees clockwise.

# Code
# def rotate_matrix(matrix):
#     return [list(row) for row in zip(*matrix[::-1])]


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(rotate_matrix(matrix))
# Output
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Search Element in Matrix
# Problem Statement

# Given a matrix and a target value, return the row and column where the target occurs. Return [-1, -1] if it doesn't exist.

# Code
# def search_matrix(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == target:
#                 return [i, j]

#     return [-1, -1]


# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# print(search_matrix(matrix, 50))
# Output
# [1, 1]

# Spiral Matrix
# Problem Statement

# Given a matrix, return its elements in spiral order, starting from the top-left corner and moving clockwise.

# Code
# def spiral_order(matrix):
#     result = []

#     if not matrix:
#         return result

#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1

#     while top <= bottom and left <= right:

#         for j in range(left, right + 1):
#             result.append(matrix[top][j])

#         top += 1

#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])

#         right -= 1

#         if top <= bottom:
#             for j in range(right, left - 1, -1):
#                 result.append(matrix[bottom][j])

#             bottom -= 1

#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])

#             left += 1

#     return result


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(spiral_order(matrix))
# Output
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Matrix Addition
# Problem Statement

# Given two matrices of the same dimensions, add them element by element.

# Code
# def add_matrices(A, B):
#     rows = len(A)
#     cols = len(A[0])

#     result = [[0] * cols for _ in range(rows)]

#     for i in range(rows):
#         for j in range(cols):
#             result[i][j] = A[i][j] + B[i][j]

#     return result


# A = [
#     [1, 2],
#     [3, 4]
# ]

# B = [
#     [5, 6],
#     [7, 8]
# ]

# print(add_matrices(A, B))
# Output
# [[6, 8], [10, 12]]

# Matrix Maximum Element
# Problem Statement

# Find the largest element in a matrix.

# Code
# def matrix_max(matrix):
#     maximum = matrix[0][0]

#     for row in matrix:
#         for value in row:
#             if value > maximum:
#                 maximum = value

#     return maximum


# matrix = [
#     [3, 8, 2],
#     [10, 5, 7],
#     [4, 6, 9]
# ]

# print(matrix_max(matrix))
# Output
# 10