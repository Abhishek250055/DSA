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
class Solution:
    def height(self, root):
        if root is None:
            return 0
        return  (1+max(self.height(root.left),self.height(root.right)))

#1st tree
root1=tree(20)
root1.insert(10)
root1.insert(9)
root1.insert(14)
root1.insert(16)
root1.insert(12)


ob = Solution()
print(f"THe height of this tree is--> {ob.height(root1)}")


#2st tree
root2=tree(20)
root2.insert(13)
root2.insert(95)
root2.insert(145)
root2.insert(165)
root2.insert(1002) 
root2.insert(18) 
root2.insert(8) 
ob = Solution()
print(f"THe height of this tree is--> {ob.height(root2)}")


