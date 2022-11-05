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
# _____________________________
f=tree(13)
f.insert(11)
f.insert(9)
f.insert(14)
f.insert(16)
f.insert(12)
f.ioprint()

        