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
        This method is a recursive function that retrieves the value of the nth node
        in a singly linked list. It checks if the current node exists and uses a base
        case where if the count (which starts at 0) equals the index, it returns the
        value of that node. Otherwise, it calls itself with the next node and a
        decremented index until the base case is met.

        Time Complexity: O(n), where n is the index of the desired node.
                         The function will be called recursively n times until it
                         reaches the desired node.

        Space Complexity: O(n), where n is the index of the desired node.
                          This is due to the recursive calls adding to the call stack.
                          Each recursive call uses space on the call stack, and there
                          will be n calls in the stack at the deepest point of recursion.
        """
    if node:
        count = 0
        if count == index:
            return node.val
        return get_nth_node(node.next, index - 1)


val = get_nth_node(node1, 1)
print(val)
