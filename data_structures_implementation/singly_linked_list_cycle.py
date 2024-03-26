# Singly linked list class

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


# Individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Construction of linkedlist cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

"""
Linked List Structure:
1 -> 2 -> 3 -> 4
       ^        |
       |________|

Explanation:
- The linked list starts at node1 with the value 1.
- It progresses to node2 (value 2), then to node3 (value 3), and then to node4 (value 4).
- Instead of terminating or linking to a null next node, node4 links back to node2, creating a cycle.
- This cycle means that traversing the list from node1 will never reach an end, as it will loop from node4 back to node2 indefinitely.
"""
