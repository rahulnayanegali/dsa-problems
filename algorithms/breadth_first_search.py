from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
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

    def bfs(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            current = queue.pop()
            print(current.value, end="\n")

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def bfs_level(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                current = queue.pop(0)
                level_nodes.append(current.value)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            print(level_nodes)

    def reverse_bfs(self):
        if self.root is None:
            return

        queue = [self.root]
        stack = []
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                current = queue.pop(0)
                level_nodes.append(current.value)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            stack.append(level_nodes)  # Push the current level to the stack

        while stack:
            level_nodes = stack.pop()
            print(level_nodes)


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("BFS traversal of the tree is:")
tree.bfs()
print("*****", end="\n")
tree.bfs_level()
print("*****", end="\n")
tree.reverse_bfs()