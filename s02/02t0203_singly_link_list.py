# importando clase node
from s02t0201_linked_list import Node

#1 creo una funcoin principal
def mian():
# 2 coloco el codigo ejecutable    
 test_node = Node("Prueba")

print(f"valor del node: {test_node.data}")

# evaluo el valor de __name__
if __name__ == "__main__":
 mian()