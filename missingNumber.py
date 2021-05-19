def missingNumber(nums):
    currentsum=sum(nums)
    n=len(nums)
    intendedsum=n*(n+1)/2
    
    
    return int(intendedsum-currentsum)
    

nums = [0,2,5,7,3,1,4]
a = missingNumber(nums)
print(a)


