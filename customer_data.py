#store data in an avl tree

import sys

#[ name, mail, phone, seats, slot, id]

# Create a tree node
class Customer():
    def __init__(self, customer_details):

        self.key = customer_details[5]

        self.name = customer_details[0]
        self.mail = customer_details[1]
        self.phone = customer_details[2]
        self.seats = customer_details[3]
        self.slot = customer_details[4]

        self.left = None
        self.right = None

        self.height = 1


class CustomerData_Tree():

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def search_seats(self,root,key):

        if root is None or root.key == key:
            return root.seats

        if root.key < key:
            return self.search_seats(root.right,key)

        return self.search_seats(root.left,key)

    def search_slot(self,root,key):

        if root is None or root.key == key:
            return root.slot

        if root.key < key:
            return self.search_slot(root.right,key)

        return self.search_slot(root.left,key)

    def insert_node(self, root, _details):

        key = _details[5]
        if not root:
            return Customer(_details)
        elif key < root.key:
            root.left = self.insert_node(root.left, _details)
        else:
            root.right = self.insert_node(root.right, _details)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete_node(self, root, key):

        if not root:            
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def preorder_traversal(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)




