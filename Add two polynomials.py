def add_polynomials(poly1, poly2):
    n = max(len(poly1), len(poly2))
    result = [0] * n
    for i in range(len(poly1)):
        result[i] += poly1[i]
    for i in range(len(poly2)):
        result[i] += poly2[i]
    return result

# Example (coefficients from lowest power)
print(add_polynomials([5, 0, 10, 6], [1, 2, 4]))  # [6, 2, 14, 6]
