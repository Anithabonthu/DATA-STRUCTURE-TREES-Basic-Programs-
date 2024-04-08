#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node: 
    def __init__(self,value): 
        self.left=None 
        self.data=value 
        self.right=None 

l=[]
class BinarySearchTree: 
    def __init__(self): 
        self.root=None       
    def insert(self,value): 
        newnode=Node(value) 
        if self.root is None: 
            self.root=newnode 
        else: 
            current=self.root 
            while True: 
                if value<current.data: 
                    if current.left is None: 
                        current.left=newnode 
                        break 
                    else: 
                        current=current.left 
                elif current.data<value: 
                    if current.right is None: 
                        current.right=newnode 
                        break 
                    else: 
                        current=current.right 
                else: 
                    break 
         
    def inorder(self,current): 
        if current: 
            self.inorder(current.left) 
            l.append(current.data) 
            self.inorder(current.right) 
def absolute_difference(l):
    ans=float("inf")
    for i in range(1,len(l)):
        ans=min(ans,l[i]-l[i-1])
    return ans

bt=BinarySearchTree() 
while True: 
    print("1.insert  2.exit") 
    ch=int(input("Enter your choice:")) 
    if ch==1: 
        value=int(input("Enter value:")) 
        bt.insert(value) 
    elif ch==2: 
        break
bt.inorder(bt.root)
print(l)
print("The Minimum Absolute Difference Between Any Two Nodes is :",absolute_difference(l))
       

