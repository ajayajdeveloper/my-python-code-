from collections import defaultdict
def conatainsDuplicate(nums):
    m=defaultdict(int)
    for num in nums:
        if m[num]:
            return True
        m[num]+=1
    return False

nums=[1,2,3,1]
a=conatainsDuplicate(nums)
print(a)