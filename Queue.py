class Queue:
    def __init__(self):
        self.q=[]
        
    def enqueue(self,x):
        self.q.append(x)
        return x
    def dequeue(self):
        if (len(self.q)>0):
            return self.q.pop(0)
            
            
    def front(self):
        if(len(self.q)==0):
            return None
        return self.q[0]
      
q=Queue()

a=q.enqueue(10)
b=q.enqueue(20)
c=q.dequeue()
d=q.front()

print(a,b,c,d)
        