from binary_search_tree import *
from random import randint

B = BST[int]()
for i in range(10):
	r = randint(1, 100)
	print(f"r: {r}")
	B.add_node(r)
	B.traverse_BST(B.root, [], out= False, order= 'post')
	print("")

if B.root != None:
	print(B.root.data)