
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
                           56, 5555, 12, 99, 45])

# intencion automatica
# for num in my_array: 
#     print(num)
# # acceso individual a los elemtos
# print(my_array[0]) # primer elemento
# print(my_array[1]) #segundo elemnto
# print(my_array[1]) # tercer elemto 

# print(len[my_array])

# interar por indices
for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
        print(f"Elemento Num {i+1}:{my_array[i]}")
