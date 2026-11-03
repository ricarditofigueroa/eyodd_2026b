class Node:
 # constructor
 def __init__(self, data=None):
   self.data = data
   self.next = None

# testiar nuetra clase none
node_01 = None ("eggs")
node_02 = None ("ham")
node_03 = None ("bacon")
print("NODES")
print(f"None 01: D: {node_01.data} - N:{node_01.next}")
print(f"None 02: D: {node_02.data} - N:{node_02.next}")
print(f"None 03: D: {node_03.data} - N:{node_03.next}")

# enlazados los nodos
node_01.next = node_02
node_02.next = node_03

print("NODES ENLAZADOS")
print(f"None 01: D: {node_01.data} - N:{node_01.next}")
print(f"None 02: D: {node_02.data} - N:{node_02.next}")
print(f"None 03: D: {node_03.data} - N:{node_03.next}")