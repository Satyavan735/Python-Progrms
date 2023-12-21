#04)Write Python program for inserting an element into binary tree.
#Python program to demonstrate insert operation in binary tree.
class BST_Node:
        def __init__(self,val):
                self.val=val
                self.left=None
                self.right=None
#A function to insert a new node
        def insert_Node(self,New_Node):
                if self.val is None:
                        self.val=New_Node
                        return
                if self.val==New_Node:
                    return
   
                        
                if self.val>New_Node:
                        if self.left is None:
                                self.left=BST_Node(New_Node)
                                
                        else:
                                self.left.insert_Node(New_Node)
                                
                else:
                        if self.right is None:
                                
                                self.right=BST_Node(New_Node)
                        else:
                                self.right.insert_Node(New_Node)
                                
#A function for inorder tree traversal
def inorder_Tree(root):
        if root:
                inorder_Tree(root.left)
                #print(root.val)
                li1.append(root.val)
                inorder_Tree(root.right)
li=[]
#root means self because selft represent object itself.
root=BST_Node(int(input("Enter a node value:")))
R=int(input("Enter range of list:"))
li.append(root.val)
for i in range(R):
        li.append(int(input("Enter a node value:")))

print("List of nodes before inorder traversal:",li)
li1=[]
for i in li:
        root.insert_Node(i)
                                
#inorder_Tree(root)                  
#print(li1)
root.insert_Node(int(input("\nEnter a new node value:")))
inorder_Tree(root) 
print("After inorder traversal:",li1)

