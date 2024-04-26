class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.value:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        elif data > node.value:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    # Search
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Deletion
    def delete(self, value):
        return self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # finding the minimum from right sub tree
            else:

                cur = node.right
                while cur.left:
                    cur = cur.left
                node.value = cur.value
                node.right = self._delete_recursive(node.right, node.value)
        return node

    # Traversing
    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.value, end=" ")


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Traversals
print("Inorder traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]
print("Preorder traversal:", bst.preorder_traversal())  # Output: [50, 30, 20, 40, 70, 60, 80]
print("Postorder traversal:", bst.postorder_traversal())  # Output: [20, 40, 30, 60, 80, 70, 50]

# Search
print(bst.search(30))  # Output: <__main__.TreeNode object at 0x7f1c8c8f2e50>x
print(bst.search(90))  # Output: None

# Delete
bst.delete(20)
bst.delete(30)
print("Inorder traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]
