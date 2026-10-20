from array import array as arr

# imprimiendo de una tabla
def print_table(input_table):
    # imprime cada eelmto
    for row in input_table:
        for column in row:
            print(column, end=",")
        print("\b ") 

table = [
    arr('i',[1,2,3]),
    arr('i',[4,5,6]),
    arr('i',[7,8,9]),
]

print_table(table)

# inserccion
row = 1
column = 2
value = 99

#insertar en la dila 1 columna 2 el valor de 99
table[row].insert(column, value)

#imprimiendo menssaje
print("--- DESPUES DE LA INSERCION del elemnto ---")
print_table(table) #DRY

# insertando una fila completa 
new_row = arr('i',[100, 200, 300])
pos  = 1
table.insert(pos, new_row)

#imprimiendo menssaje
print("--- DESPUES DE LA INSERCION de la fila ---")
print_table(table) #DRY
   
#eliminacion de elemento
del table[2] 

#imprimiendo menssaje
print("--- DESPUES DE LA eliminacion de la fila 2 ---")
print_table(table) #DRY