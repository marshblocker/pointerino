from __future__ import annotations
from typing import Generic, Optional, TypeVar


T = TypeVar("T", int, float, str)
V = TypeVar("V", int, float, str)


class Node(Generic[T]):
    def __init__(self, data: T, next: Optional[Node[T]] = None):
        self.data: T = data
        self.next: Optional[Node[T]] = next


class BSTNode(Generic[V]):
    def __init__(self, data: V,
                 left: Optional[BSTNode[V]] = None,
                 right: Optional[BSTNode[V]] = None):
        self.data = data
        self.left = left
        self.right = right
