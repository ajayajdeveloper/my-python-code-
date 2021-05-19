class plateStack:
    def __init__(self):
        self.st=[]
        
    def Push(self,x):
        self.st.append(x)
        return x
        
    def Pop(self):
        if(len(self.st) > 0):
           return self.st.pop()
            
        

    def Top(self):
        if(len(self.st)==0):
            return None
        return self.st[-1]
    
    def Getlen(self):
        return len(self.st)
    
    
s=plateStack()

a=s.Push(1)
e=s.Push(2)
z=s.Push(5)
c=s.Top()
d=s.Getlen()
b=s.Pop()

print(a)
print(b)
print(c)
print(d)
print(e)
print(z)
    