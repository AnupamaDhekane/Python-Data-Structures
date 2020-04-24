class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            print("Adding the first node of the tree")
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, currentnode: Node):
        """

        :type data: object
        """
        if currentnode.data < data:
            if currentnode.right is None:
                currentnode.right = Node(data)
            else:
                currentnode = currentnode.right
                self._insert(data, currentnode)
        elif currentnode.value > data:
            if currentnode.left is None:
                currentnode.left = Node(data)
            else:
                self._insert(data, currentnode.left)
        else:
            print("The node is already in the tree.")
