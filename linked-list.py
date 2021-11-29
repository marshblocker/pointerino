from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
	data: T 
	next: Optional[Node[T]] = None

@dataclass
class LinkedList(Generic[T]):
	head: Optional[Node[T]] = None

	def add_node(self, new: Node[T]) -> None:
		""" 
		Assign new as the head node of the linked list.
		"""
		new.next = self.head
		self.head = new

	def delete_node(self, target: T, all: bool = False) -> None:
		"""
		Delete the first discovered node with data == target from the 
		linked list. If the all flag is set to True, delete all nodes with 
		data == target. If no nodes in the linked list have their data member 
		equal to target, this method performs no action.
		"""
		alpha = self.head
		beta: Optional[Node[T]] = None

		found: bool = False 

		while alpha != None:
			if alpha.data == target:
				if beta == None:  # target node is the head node
					self.head = alpha.next 
				else:
					beta.next = alpha.next

				found = True 
				if not all:
					break

			beta = alpha 
			alpha = alpha.next

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
		gamma: Optional[Node[T]] = None 

		while beta != None:
			beta.next = gamma 
			gamma = beta 
			beta = alpha 
			if alpha != None:
				alpha = alpha.next
		self.head = gamma 

		return 

