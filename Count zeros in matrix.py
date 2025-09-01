def count_zeros(matrix):
    return sum(row.count(0) for row in matrix)

# Example
print(count_zeros([[0,0,1],[0,1,1],[1,1,1]]))  # 3
