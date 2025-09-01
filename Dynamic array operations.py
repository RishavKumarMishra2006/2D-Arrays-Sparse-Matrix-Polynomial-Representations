def dynamic_array(n, queries):
    seq = [[] for _ in range(n)]
    last_answer = 0
    results = []
    for t, x, y in queries:
        idx = (x ^ last_answer) % n
        if t == 1:
            seq[idx].append(y)
        elif t == 2:
            last_answer = seq[idx][y % len(seq[idx])]
            results.append(last_answer)
    return results

# Example
q = [(1, 0, 5), (1, 1, 7), (1, 0, 3), (2, 1, 0), (2, 1, 1)]
print(dynamic_array(2, q))  # [7, 3]
