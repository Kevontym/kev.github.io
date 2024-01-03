class Node:
    def __init__(self, data):
        self.data = data  # data stored in the node
        self.next = None  # reference to the next node

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes in a linked list
node1.next = node2
node2.next = node3

