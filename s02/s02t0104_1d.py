from array import array as arr

# importar una funcion de otro
# archivo
from s02t0102_1d import print_array

my_array = arr('i', [2, 10, 15, 20, 10])

print("--- ANTES DE LA INSERCION ---")
print_array(my_array)

# eliminacion
try:
 while 10 in (my_array):
  my_array.remove(10)
except:
 print(f"no se encuentra en ek arreglo") 
print("--- DESPUES DE LA ELIMINACION ---")
print_array(my_array)


