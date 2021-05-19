class MinStack:
    def __init__(self):
        self.st=[]
        
    def Push(self,x):
        curmin=self.getMin()
        if curmin==None or curmin > x:
            curmin = x
        return self.st.append((x,curmin))
        
    def pop(self):
        return self.st.pop()
        
    def top(self):
        return self.st[-1][0] if self.st else None
    
    def getMin(self):
        return self.st[-1][1] if self.st else None
        
m=MinStack()

a=m.Push(10)
a1=m.Push(5)
b=m.pop()
c=m.top()
d=m.getMin()


print(a,b,a1,c,d)