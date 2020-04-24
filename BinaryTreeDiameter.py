class Node:
    def __init__(self,data = None):
        self.val = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self,data = None):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, currentnode):
        if data > currentnode.val:
            if currentnode.right is None:
                currentnode.right = Node(data)
            else:
                self._insert(data,currentnode.right)
        else:
            if currentnode.left is None:
                currentnode.left = Node(data)
            else:
                self._insert(data,currentnode.left)

    
    def height(self, currentnode):
        if currentnode.val = None:
            return 0
        else:
            lh = self.height(currentnode.left)
            rh = self.height(currentnode.right)

            return 1+ max(lh,rh)

    def find_diameter(self, rootnode):
        if rootnode is None:
            return 0
        else:
            lh = self.height(rootnode.left)
            rh = self.height(rootnode.right)

            ldiameter = self.find_diameter(rootnode.left)
            rdiameter = self.find_diameter(rootnode.right)

            return max(lh+rh+1,max(ldiameter,rdiameter))
