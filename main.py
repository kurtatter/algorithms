from algol import Algol
from structure import Node

import matplotlib.pyplot as pyplot


def show_node():
    ll = Node(1)
    ll.append(3)
    ll.append(5)
    ll.append(7)

    def last_node(nodes: Node):
        while nodes.next:
            nodes = nodes.next
        return nodes.data

    print(last_node(ll))


def main():
    import random
    nums = [random.randint(1, 20) for _ in range(10)]
    print(Algol.recursion_nod(50, 25))


if __name__ == '__main__':
    main()
