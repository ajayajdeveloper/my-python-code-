class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class levelOrder:
    def levelorder(self,root:Tree)
        ans=[]
        if(root is None):
            return ans
        
        q=deque([root]) 
        
        while(q):
            n=len(q)
            temp=[]
            for i in range(0,n):
                f=q.popleft()
                temp.append(f.val)
                
                if(f.left is not None):
                    q.append(f.left)
                if(f.right is not None):
                    q.append(f.right)
                    
                if(len(temp) > 0):
                    ans.append(temp[:])
                    temp.clear()
                    
        return ans
    
root=[3,9,20,None,None,15,7]
l=levelOrder()
a=l.levelorder(root)
print(a)