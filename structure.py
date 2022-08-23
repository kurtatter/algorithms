class LinkedList:
    ...


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        head = self
        while head.next:
            head = head.next
        head.next = end
