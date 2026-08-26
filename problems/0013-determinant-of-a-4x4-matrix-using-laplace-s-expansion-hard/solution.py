def determinant_4x4(matrix: list[list[int | float]]) -> float:
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(n):
        minor = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]

        det += (-1) ** col * matrix[0][col] * determinant_4x4(minor)

    return det