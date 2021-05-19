def moveZeroes(nums):
    
    j = 0
    for num in nums:
        if(num != 0):
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0
        
    return nums



    
nums=[0,1,0,10,20]    
result = moveZeroes(nums)

if result != -1:
    print(str(nums))


            
         


    



