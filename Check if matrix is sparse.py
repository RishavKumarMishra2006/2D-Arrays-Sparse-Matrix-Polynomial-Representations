def is_sparse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    total = rows * cols
    zero_count = sum(1 for i in range(rows) for j in range(cols) if matrix[i][j] == 0)
    return zero_count > total / 2

# Example
print(is_sparse([[0,0,3],[0,0,0],[4,0,0]]))  # True
