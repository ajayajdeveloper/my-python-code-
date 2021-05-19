def lengthOfLengthSubstring(s):
    m={}
    left = 0
    right = 0 
    ans = 0
    n = len(s)
    
    while(left < n and right < n):
        el = s[right]
        if(el in m ):
            left = max(left,m[el]+1)
        m[el] = right
        ans = max (ans,right-left+1)
        right +=1
        
    return ans 

s=[1,2,3,4,5,7,8,9,10,1,1,2,3,4,5]
a = lengthOfLengthSubstring(s)
print(a)



