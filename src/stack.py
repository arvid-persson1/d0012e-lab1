from typing import Optional

class Node[T]:
    item: T
    # See PEP 484 @ "The problem of forward declarations"
    next: Optional['Node[T]']

    def __init__(self, item: T):
        self.item = item
        self.next = None

class LinkedList[T]:
    head: Optional[Node[T]] = None

    def push_front(self, item: T):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head

    def pop_front(self) -> Optional[T]:
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self) -> bool:
        return self.head is None

class Stack[T]:
    inner: LinkedList[T]

    def __init__(self):
        self.inner = LinkedList()

    def push(self, item: T):
        self.inner.push_front(item)

    def pop(self) -> Optional[T]:
        return self.inner.pop_front()

    def is_empty(self) -> bool:
        return self.inner.is_empty()
