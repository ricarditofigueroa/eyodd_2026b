from array import array as arr
# parametrso de mi cuadricula
rows = 8
columns = 2 * rows - 1

# crean la grid 2D
matrix = []

# construyendo el grid
for _ in range(rows):
    new_row = arr('i',[0] * columns)
    matrix.append(new_row)

#validando la construccion del grid
print(f"Cantidad de filas: len(matrix)")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))
