from ds.linked_list import *

def test():
	A = LinkedList[int]()

	print("Populating...")
	A.traverse_linked_list()
	for i in range(10):
		A.add_node(i)
		A.traverse_linked_list()
		A.reverse_linked_list()
		A.traverse_linked_list()
		A.reverse_linked_list()

	print("Erasing...")
	A.traverse_linked_list()
	for i in range(10):
		A.delete_node(i)
		A.traverse_linked_list()
		A.reverse_linked_list()
		A.traverse_linked_list()	
		A.reverse_linked_list()