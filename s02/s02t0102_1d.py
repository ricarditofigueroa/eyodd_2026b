# import el mudulo array de
#  la bibloteca array y creando como arr
from array import array as arr

def print_array(input):
    print("[", end="")
    for element in input:
        print(element, end=',')
    print("\b]")
    

my_array = arr('i', [2, 10, 15, 20])
print_array(my_array)

# buscar el elemento 15
number_to_search = 15
counter = 0
print(f"se busca {number_to_search} en el arreglo.")
for integer in my_array:
    if integer == number_to_search:
        print("Numero encontrado")
        # sirve para terminar el ciclo
        break
   # contador 
counter+=1
if counter == len(my_array):
    print("😒numero no encontrado") 