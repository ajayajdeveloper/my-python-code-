def twoSum(nums,target):
    m={}
    n=len(nums)
    for i in range(0,n):
        goal=target-nums[i]
        if(goal in m):
            return[m[goal],i]
        m[nums[i]]=i
        
nums=[3,6,12,14]
target=15

a=twoSum(nums,target)
print(a)