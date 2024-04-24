class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev  # Reverse the link
        prev = curr  # Move prev and curr pointers
        curr = next_node

    return prev


def createLinkedList(lst):
    dummy = Node()
    curr = dummy
    for val in lst:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    curr = head
    lst = []
    while curr:
        lst.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(lst))


head = createLinkedList([1, 2, 3, 4, 5])
print("Original List: ", end="")
print_linked_list(head)
reversed_head = reverse_linked_list(head)
print("Reversed List: ", end="")
print_linked_list(reversed_head)
print()