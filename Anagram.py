def findHash(s):
    return "".join(sorted(s))

def groupAnagrams(strs):
    answers=[]
    m={}
    
    for s in strs:
        hashed = findHash(s)
        if (hashed not in m):
            m[hashed]=[]
        m[hashed].append(s)
            
    for p in m.values():
        answers.append(p)
        
    return answers

strs=["eat","ate","bat"]
a=groupAnagrams(strs)
print(a)