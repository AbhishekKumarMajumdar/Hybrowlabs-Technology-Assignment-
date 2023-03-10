# Implement a binary search tree (BST) data structure in Python. The BST should support the following operations:
# insert(item) - Insert an item into the tree.
# delete(item) - Remove an item from the tree.
# search(item) - Return True if the item is in the tree, else False.
# size() - Return the number of nodes in the tree.

'''Solution'''

class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def Insert(self,Item):
        if self.key is None:
            self.key = Item
            return
        elif self.key==Item:
            return
        elif self.key>Item:
            if self.left:
                self.left.Insert(Item)
            else:
                self.left = BST(Item)
        else:
            if self.right:
                self.right.Insert(Item)
            else:
                self.right = BST(Item)
    def Search(self,Item):
        if self.key == Item:
            return print("True")
        elif self.key > Item:
            if self.left:
                self.left.Search(Item)
            else:
                return print("False")
        else:
            if self.right:
                self.right.Search(Item)
            else:
                print("Node not Found in this tree")

    def Delete(self,Item):
        if self.key is None:
            print("Tree is Empty")
            return
        elif self.key>Item:
            if self.left : 
                self.left = self.left.Delete(Item)
            else:
                print("Given Node is not Prasant in this Tree")

        elif self.key<Item:
            if self.right : 
                self.right = self.right.Delete(Item)
            else:
                print("Given Node is not Prasant in this Tree")
        
        else:
            if self.left is None :
                temp = self.right
                self = None
                return temp
            elif self.right is None :
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.Delete(node.key)
        return self

    def PreOrder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.PreOrder()
        elif self.right:
            self.right.PreOrder()

    def Size(self):
        if self.left and self.right:
              return 1 + self.left.Size() + self.right.Size()
        elif self.left:
            return 1 + self.left.Size()
        elif self.right:
            return 1 + self.right.Size()
        else: return 1

root_choose = int(input("enter the Root Node\n"))
root = BST(root_choose)

while True:
    print("Implement a stack data structure in Python")
    choose = input("Enter your Operation (Insert , Delete , Size , Search , exit \n").lower()
    if(choose=='insert'):
        data = int(input("Enter the Item \n"))
        root.Insert(data)
        print(data,"is Insert in Binary Search Tree")
        input("enter to continue")
    if 'delete' in choose:
        data = int(input("Enter the Item For Delete in Binary Search Tree \n"))
        root.Delete(data)
        print("%d is Deleted in Binary Search Tree "%data)
        input("enter to continue")

    if  'size' in choose:
        print(root.Size(),"Nodes in the tree\n")
        input("enter to continue")

    if  'search' in choose:
        data = int(input("Enter the Item to Search in Binary Search Tree \n"))
        root.Search(data)


    if 'exit' in choose:
        break