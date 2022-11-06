# Explanation: The tree is
#    1    (mirror)  1
#  /  \    =>      /  \
# 2    3          3    2
# The inorder of mirror is 3 1 2

class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#insert in tree__________________
    def insert(self,n_data):
        if n_data<=self.data:
            if self.left==None:
                self.left=tree(n_data)
            else:
                self.left.insert(n_data)
        else:
            if self.right==None:
                self.right=tree(n_data)
            else:
                self.right.insert(n_data)

# ____________________inoder_print data________________
    def ioprint(self):
        if self.left!=None:
            self.left.ioprint()
        print("-->",self.data)
        if self.right!=None:
            self.right.ioprint()
# _______________________________________________

class Solution():
    def mirror(self,root):
        if root is None:
            return 0;
        self.mirror(root.left)
        self.mirror(root.right)
        
        temp=root.left
        root.left=root.right
        root.right=temp


#1st tree
root1=tree(10)
root1.insert(21)
root1.insert(3)

root1.ioprint()

ob = Solution()
ob.mirror(root1)
print("This is the inorder of mirror tree")

root1.ioprint()