def rotate_90(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

# Example
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_90(mat))  
# [[7,4,1],[8,5,2],[9,6,3]]
