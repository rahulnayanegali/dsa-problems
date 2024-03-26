# Singly linked list class
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


# Individual nodes
node1 = ListNode(1)
node2 = ListNode(10)
node3 = ListNode(30)
node4 = ListNode(40)

# Construction of linkedlist
node1.next = node2
node2.next = node3
node3.next = node4


def get_nth_node(node, index):
    """
        This method traverses the linked list from the head node to the nth node
        and returns the value of the nth node. It uses a counter to keep track of
        the current node index as it iterates through the list.

        Time Complexity: O(n), where n is the index of the desired node.
                         This is because, in the worst case, the function will have to
                         traverse n nodes to reach the desired node.

        Space Complexity: O(1), as no additional space is used proportional to the
                          input size. The space used is constant regardless of the
                          size of the linked list.
        """
    count = 0
    current = node
    while current:
        if count == index:
            return current.val
        count += 1
        current = current.next


val = get_nth_node(node1, 1)
print(val)
