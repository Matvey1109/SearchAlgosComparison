class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while True:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right


def tree_linear_search(root, data):
    if root is None:
        return None

    stack = [root]

    while stack:
        node = stack.pop()
        if node.data == data:
            return node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return None


def tree_binary_search(root, data):
    while root is not None:
        if root.data == data:
            return root
        elif data < root.data:
            root = root.left
        else:
            root = root.right
    return None


def tree_interpolation_search(root, data):
    if root is None:
        return None

    node = root
    while node is not None:
        if node.data == data:
            return node
        elif data < node.data:
            if node.left is None:
                return None
            node_low = node.left
            node_high = node
        else:
            if node.right is None:
                return None
            node_low = node
            node_high = node.right

        if node_high.data == node_low.data:
            return None

        mid = node_low.data + (
            (data - node_low.data) * (node_high.data - node_low.data)
        ) // (node_high.data - node_low.data)
        mid_node = root
        while mid_node.data != mid:
            if mid < mid_node.data:
                mid_node = mid_node.left
            else:
                mid_node = mid_node.right

        if mid_node.data == data:
            return mid_node
        elif mid_node.data < data:
            node = mid_node.right
        else:
            node = mid_node.left

    return None
