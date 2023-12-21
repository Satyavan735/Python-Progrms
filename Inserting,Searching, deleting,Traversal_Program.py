# Python program for Inserting,Searching, deleting and 
#Traversal (Inorder,Preorder,Postorder)an element from binary tree.
#Tree Traversal Program
class BST_Tree:
    def __init__(self,value):
        self.lchild=None
        self.rchild=None
        self.value=value
    #Inserting new node in BST
    def insert_node(self,data):
        if self.value is None:
            self.value=data
        elif self.value ==data:
            return
        elif self.value>data:
            if self.lchild is None:
                self.lchild=BST_Tree(data)
            else:
                self.lchild.insert_node(data)
        else:
            if self.rchild:
                self.rchild.insert_node(data)
            else:
                self.rchild=BST_Tree(data)

    def Search(self,data):
        if self.value==data:
            print("Node is found!....")
        if data<self.value:
            if self.lchild:
                self.lchild.Search(data)
            else:
                print("Node is not present in given tree!...")
        if data>self.value:
            if self.rchild:
                self.rchild.Search(data)
            else:
                print("Node is not presen in given tree!...")
                
    def delete_node(self,data):
        if self.value is None:     #Check Tree is empty or not
            print("Tree is empty")
        elif data<self.value:     #Find the position of the given node
            if self.lchild:
                self.lchild=self.lchild.delete_node(data)
            else:
                print("Given node is not presernt in tree..")
        elif data>self.value:
            if self.rchild:
                self.rchild=self.rchild.delete_node(data)
            else:
                print("Given node is not present in tree..")
        else:  #Node value store in self.lchild ,Check it contain 0,1 or 2 child 
            if self.lchild is None: #---
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp= self.lchild
                self=None
                return temp #--Delete operation for node have 0 and 1 child
            #Delete operation for node have 2 child
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.value=node.value
            self.rchild=self.rchild.delete_node(node.value)
        return self
        #Traversal methods
        #Inorder Traversal
    def Inorder(self):
        if self.lchild:
            self.lchild.Inorder()
        print(self.value,end="==> ")
        if self.rchild:
            self.rchild.Inorder()
    def Preorder(self):
        print(self.value,end="==> ")
        if self.lchild :
            self.lchild.Preorder()
        if self.rchild:
            self.rchild.Preorder()
    def Postorder(self):
        if self.lchild:
            self.lchild.Postorder()
        if self.rchild:
            self.rchild.Postorder()
        print(self.value,end="==>")

R=int(input("Enter range for list:"))    
root=BST_Tree(int(input("Enter a node value:")))
li=[]
li.append(root.value)
for i in range(R):
    li.append(int(input("Enter a node value:")))
print("\n",li)
for i in li:
    root.insert_node(i)

print("\nPreorder Traversal")
root.Preorder()
print("\nInorder Traversal")
root.Inorder()
print("\nPostorder Traversal")
root.Postorder()
print("\n Search method.")
root.Search(int(input("Enter a node for search operation:")))

print("\nDelete method!...")
root.delete_node(int(input("Enter node that you want to delete:")))
print("\nAfter deleting...")
root.Preorder()


        

            
            
            
