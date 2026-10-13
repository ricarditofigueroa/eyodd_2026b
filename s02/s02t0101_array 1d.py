
# array
# from array import
import array as arr

# creacion de un arreglo
#i: entero con signo
#I: entero sin signos
#f: numero decimal
#d: numero desimal doble 
#u: caracteres unicode
my_array = arr.array('i', [10, 22, 300, 22, 333, 
                           56, 5555, 2000, 99, 45])

# intencion automatica
# for num in my_array: 
#     print(num)
# # acceso individual a los elemtos
# print(my_array[0]) # primer elemento
# print(my_array[1]) #segundo elemnto
# print(my_array[1]) # tercer elemto 

# print(len[my_array])

# interar por indices
# for i in range(len(my_array)):
#     if my_array[i] % 2 == 0:
#         print(f"Elemento Num {i+1}:{my_array[i]}")

#Busqueda de un elemento
num_to_search = 2000

# modificando un valor
# bracket notation
my_array[8] = 2000
try:
    print(f"Localizado {num_to_search}: {my_array.index(num_to_search)}")
except:
    print(f" ⚠️ numero no encontrado !!!")

# asignando valor en un indice que no exista
try:
 my_array[100] = 3 
except:
  print(" ⚠️ indice no existe !!!") 