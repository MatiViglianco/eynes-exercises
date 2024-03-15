def transpose(matrix):
    transposed_matrix  = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            transposed_matrix[column][row] = matrix[row][column]
    matrix[:] = transposed_matrix
    return matrix