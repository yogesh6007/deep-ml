import numpy as np

def row_normalize(counts):
    counts = np.array(counts, dtype=float)

    # Keep row sums as a column vector: shape (n, 1)
    row_sums = counts.sum(axis=1, keepdims=True)

    # Avoid division by zero for rows whose sum is 0
    row_sums[row_sums == 0] = 1

    # Broadcasting divides each row by its corresponding row sum
    probabilities = counts / row_sums

    return probabilities.tolist()