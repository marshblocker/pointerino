from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
	data: int 
	next: Optional[Node] = None

@dataclass
class LinkedList:
	head: Optional[Node] = None

	def add_node(self, new: Node) -> None:
		""" 
		Assign new as the head node of the linked list.
		"""
		new.next = self.head
		self.head = new

	def delete_node(self, target: int, all: bool = False) -> None:
		"""
		Delete the first discovered node with data == target from the 
		linked list. If the all flag is set to True, delete all nodes with 
		data == target. If no nodes in the linked list have their data member 
		equal to target, this method performs no action.
		"""
		alpha = self.head
		beta: Optional[Node] = None

		found: bool = False 

		while alpha != None:
			if alpha.data == target:
				if alpha == self.head:	# target node is the head node.
					self.head = alpha.next
				else:
					assert isinstance(beta, Node)
					beta.next = alpha.next
				found = True
				print(f"{target} is successfully deleted from the Linked List.")
				if not all:
					break

			beta = alpha
			alpha = alpha.next
			assert isinstance(alpha, Optional[Node])

		if not found:
			print(f"{target} is not found in the Linked List.")
		return

	def traverse_linked_list(self) -> None:
		"""
		Print the nodes of the linked list starting from the node pointed
		to by self.head.
		"""
		t = self.head 

		while t != None:
			print(f"{t.data} -> ", end= "")
			t = t.next
		print("None")

		return 

	def reverse_linked_list(self) -> None:
		"""
		Reverse the direction of the linked list such that the head node
		now points to None and self.head now points to the tail node. If
		the linked list contains one or no node, this method performs no
		action.
		"""
		if self.head == None:
			return 

		alpha = self.head.next
		beta = self.head 
		gamma: Optional[Node] = None 

		while True:
			if alpha == None:  # reverse the last node.
				beta.next = gamma 
				self.head = beta
				break
			beta.next = gamma 
			gamma = beta 
			beta = alpha 
			alpha = alpha.next

		return 
