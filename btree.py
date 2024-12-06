# Muaaz Abed mma210009 CS 4348-502

class Node:
    def __init__(self, block_id, parent_id=0):
        self.block_id = block_id
        self.parent_id = parent_id
        self.keys = []
        self.values = []
        self.children = []
        self.is_leaf = True

    def is_full(self, degree):
        return len(self.keys) == 2 * degree - 1

class BTree:
    def __init__(self, root_block_id, degree=10):
        self.root = Node(root_block_id)
        self.degree = degree

    def insert(self, key, value):
        """Insert a key-value pair into the B-Tree."""
        if self.root.is_full(self.degree):
            new_root = Node(block_id=self.root.block_id + 1)
            new_root.is_leaf = False
            new_root.children.append(self.root)
            self.split_child(new_root, 0, self.root)
            self.root = new_root

        self.insert_non_full(self.root, key, value)

    def insert_non_full(self, node, key, value):
        """Insert a key-value pair into a non-full node."""
        if node.is_leaf:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.values.insert(i + 1, value)
            print(f"Inserted key = {key}, value = {value} in node with block ID = {node.block_id}\n")
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if node.children[i].is_full(self.degree):
                self.split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key, value)

    def split_child(self, parent, index, child):
        """Split a full child node."""
        degree = self.degree
        new_node = Node(block_id=child.block_id + 1)
        new_node.is_leaf = child.is_leaf
        new_node.keys = child.keys[degree:]
        new_node.values = child.values[degree:]

        if not child.is_leaf:
            new_node.children = child.children[degree:]
            child.children = child.children[:degree]

        parent.keys.insert(index, child.keys[degree - 1])
        parent.values.insert(index, child.values[degree - 1])
        parent.children.insert(index + 1, new_node)

        child.keys = child.keys[:degree - 1]
        child.values = child.values[:degree - 1]

        print(f"Split node {child.block_id} into nodes {child.block_id} and {new_node.block_id}")