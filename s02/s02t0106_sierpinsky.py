from array import array as arr

# parametros de mi cuadricula
rows = 10
columns = 2 * rows - 1

# funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# crear la grid 2D
matrix = []

# construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# validando la construccion del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# calculando el centro de la primera fila
center = columns // 2

# estableciendo el centro en 1
matrix[0][center] = 1

# calculando el resto de la matrix
# siguiendo la logica del sierpinski gasket
for row in range(1, rows):
    for column in range(0, columns):
        left_upper_cell = 0
        right_upper_cell = 0

        # si la columna es mayor a 0
        if column > 0:
            left_upper_cell = matrix[row - 1][column - 1]

        # si la columna esta antes del borde derecho
        if column < columns - 1:
            right_upper_cell = matrix[row - 1][column + 1]

        # guardar el resultado en la matriz
        if left_upper_cell != right_upper_cell:
            matrix[row][column] = 1
        else:
            matrix[row][column] = 0

print()
print_matrix(matrix)