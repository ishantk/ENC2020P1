"""
Tree Data Structure: BST
https://www.cs.usfca.edu/~galles/visualization/BST.html

"""

class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProductDetails(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}\t{}\t{}".format(self.pid, self.name, self.price))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class TreeNode:

    def __init__(self):
        print(">> TreeNode Created")
        self.object = None
        self.left = None
        self.right = None

    def showTreeNode(self):
        self.object.showProductDetails()
        print("LEFT:", self.left, "RIGHT:", self.right)


class Tree:

    size = 0

    def __init__(self):
        print(">> Tree Data Structure Created")
        self.rootNode = None

    def add(self, node, object):

        if node == None:
            Tree.size += 1
            tNode = TreeNode()
            tNode.object = object
            # print("^^^^^^^^^^^^^^^^^^^^^")
            # print("[NODE ADDED]")
            # tNode.showTreeNode()
            # print("^^^^^^^^^^^^^^^^^^^^^")

            return tNode

        if object.price < node.object.price:
            node.left = self.add(node.left, object)     # Insert data in Left
        else:
            node.right = self.add(node.right, object)   # Insert Data in Right

        return node

    def preOrder(self, node):

        if node != None:
            node.object.showProductDetails()
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):

        if node != None:
            self.inOrder(node.left)
            node.object.showProductDetails()
            self.inOrder(node.right)

    def postOrder(self, node):

        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            node.object.showProductDetails()

    # Use Loops and Recursion :)
    def maxNumber(self, node):
        pass

    def minNumber(self, node):
        pass


product1 = Product(101, "iPhoneX", 50000)
product2 = Product(301, "AlphaBounce", 8000)
product3 = Product(701, "Samsung LED", 40000)
product4 = Product(401, "Vivo M1", 10000)
product5 = Product(901, "Samsung M1", 60000)


tree = Tree()
tree.rootNode = tree.add(tree.rootNode, product1)
tree.add(tree.rootNode, product2)
tree.add(tree.rootNode, product3)
tree.add(tree.rootNode, product4)
tree.add(tree.rootNode, product5)

print(">> TREE SIZE:", Tree.size)

# tree.preOrder(tree.rootNode)
# tree.inOrder(tree.rootNode)
tree.postOrder(tree.rootNode)


"""
        50000
      /      \
  8000      60000
     \
     40000
       /
    10000        
   
   R'-L-R
   PreOrder : 50000 < 8000 < 40000 < 10000 < 60000 
   
   L-R'-R     
   InOrder  : 8000 < 10000 < 40000 < 50000 < 60000 
   
   L-R-R'
   PostOrder: 10000 < 40000 < 8000 < 60000 < 50000                  
        
"""
