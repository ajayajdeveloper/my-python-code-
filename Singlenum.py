def singleNumber(nums):
    
    return 2*sum(set(nums))-sum(nums)

nums=[1,2,2,5,5]
a=singleNumber(nums)
print(a)