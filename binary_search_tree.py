# Note: Work in Progress.
# TODO: Implement delete operation.

from typing import Literal
from node import *


class BST(Generic[T]):
    """
    Create a Binary Search Tree (BST). A BST is a binary tree with the
    following recursive property:

    For each non-leaf node i in the BST:
            - data(i) >= data(left_child(i))
            - data(i) < data(right_child(i))
    """

    def __init__(self):
        """ Initialize class attributes root, height, and population. """
        self.root: Optional[BSTNode[T]] = None
        self.height: int = 0
        self.population: int = 0

    def add_node(self, data: T) -> None:
        """ Create node new and add to the BST in an iterative manner. """
        new = BSTNode[T](data)
        t = self.root

        self.population += 1

        if t is None:
            self.root = new
            return
        while True:
            if new.data <= t.data:
                if t.left is None:
                    t.left = new
                    self.height += 1
                    break
                else:
                    t = t.left
            else:
                if t.right is None:
                    t.right = new
                    self.height += 1
                    break
                else:
                    t = t.right

            self.height += 1

        return

    def traverse_BST(self, curr: Optional[BSTNode[T]],
                     arrangement: list[BSTNode[T]],
                     out: bool = True,
                     order: Literal['pre', 'in', 'post'] = 'in'
                     ) -> list[BSTNode[T]]:
        """
        Traverse the BST based on the order flag. If out = False, suppress
        printing of arrangement. Return arrangement.
        """
        if curr is None:
            return arrangement

        if order == 'pre':
            if out:
                print(f"{curr.data} ", end="")
            arrangement.append(curr)

        BST[T].traverse_BST(self, curr.left, arrangement)

        if order == 'in':
            if out:
                print(f"{curr.data} ", end="")
            arrangement.append(curr)

        BST[T].traverse_BST(self, curr.right, arrangement)

        if order == 'post':
            if out:
                print(f"{curr.data} ", end="")
            arrangement.append(curr)

        return arrangement
