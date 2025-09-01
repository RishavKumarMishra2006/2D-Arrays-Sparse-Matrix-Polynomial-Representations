def sum_of_diagonals(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n-i-1] for i in range(n))
    return primary + secondary if n % 2 == 0 else primary + secondary - matrix[n//2][n//2]

# Example
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(sum_of_diagonals(mat))  # 25
