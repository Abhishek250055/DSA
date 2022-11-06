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
def cheak(root1,root2):
    if root1 is None and root2 is None:
        return True
    else:
        if root1.data==root2.data and cheak(root1.left,root2.left) and cheak(root1.right,root2.right):
            return True
        else:
            return False 
   

root1=tree(20)
root1.insert(10)
root1.insert(9)
root1.insert(14)
root1.insert(16)
root1.insert(12)

root2=tree(20)
root2.insert(11)
root2.insert(9)
root2.insert(14)
root2.insert(16)
root2.insert(12)

if cheak(root1,root2):
    print("true")
else:
    print("False")