class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, data=None):
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

    def printtree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._printtree(self.root)

    def _printtree(self,currentnode):
        if currentnode is not None:
            self._printtree(currentnode.left)
            print(str(currentnode.data))
            self._printtree(currentnode.right)

    def filltree(slef,tree,num_elem=100, max_int =1000):
        from random import randint
        for _ in range(num_elem):
            currentnode = randint(0, max_int)
            tree.insert(currentnode)
        return tree


tree = BST()


def filltree(tree):
    pass


tree = filltree(tree)
