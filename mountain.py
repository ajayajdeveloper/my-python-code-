def validMountainArray(A):
    if(len(A)<3):
        return False
    
    i=1
    
    while(i<len(A) and A[i]>A[i-1]):
        i+=1
    if(i==1 or i==len(A)):
        return False
    while(i< len(A) and A[i] < A[i-1]):
        i+=1
        
    return i==len(A)


    
A=[0,2,5,7,9,10,12]
result =validMountainArray(A)

if result==len(A):
    print("it is a mountain array")
else:
    print("it is a not  mountain array")
    