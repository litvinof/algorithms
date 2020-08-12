class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data == cur_node.data:
            print("Value is already present in the tree")
            return

        elif data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        else:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

    def find(self, data):
        is_found = self._find(data, self.root) if self.root else False
        return is_found

    def _find(self, data, cur_node):
        if cur_node:
            if data == cur_node.data:
                return True
            elif data > cur_node.data:
                return self._find(data, cur_node.right)
            else:
                return self._find(data, cur_node.left)

        return False


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

#   4
#  / \
# 2   8
#    / \
#   5  10


print(bst.find(5))
print(bst.find(11))

# import pdb; pdb.set_trace()
