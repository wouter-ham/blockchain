class Node:
    def __init__(self, data):
        self.data: int = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    # Insert at the beginning of the list
    def insertBeg(self, new_data: int) -> None:
        new_node: Node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insertEnd(self, new_data: int) -> None:
        tail: Node | None = self.getTail()
        new_node: Node = Node(new_data)
        if tail is None:
            self.head = new_node
        else:
            tail.next = new_node

    # Insert after a node
    def insertAfter(self, data: int, new_data: int) -> None:
        new_node: Node = Node(new_data)
        current: Node = self.head
        while current.data != data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Deleting a node at a specific index
    def deleteIndex(self, index: int) -> None:
        current: Node = self.head
        for _ in range(0, index - 1):
            current = current.next
        current.next = current.next.next

    # Search an element
    def find(self, key: int) -> int:
        index: int = 0
        current: Node = self.head
        while current.data != key:
            if current.next is None:
                return -1

            current = current.next
            index += 1
        return index

    # Sort the linked list
    def sort(self, head: Node) -> None:
        values: list = []
        while head.next is not None:
            values.append(head.data)
            head = head.next
        values.append(head.data)
        values.sort()

        self.head = Node(values.pop(0))
        current: Node = self.head
        for val in values:
            node: Node = Node(val)
            current.next = node
            current = current.next

    def printList(self) -> None:
        current: Node = self.head
        values: list = []
        while current.next is not None:
            values.append(current.data)
            current = current.next
        values.append(current.data)
        print(' '.join([str(i) for i in values]))

    def getTail(self) -> Node | None:
        current: Node = self.head
        if current is None:
            return None
        while current.next is not None:
            current = current.next
        return current
