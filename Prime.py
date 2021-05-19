def countPrime(n):
    if n < 2:
        return 0
    isPrime = [True]*n
    isPirme[0]= isPirme[1]= False
    
    for i in range(2,math.ceil(math.sqrt(n))):
        if isPrime[i]:
            for multiples_of_i in range (i*i,n,i):
                isPrime[multiples_of_i]=False
                
    return sum(isPrime)

n=34
r=countPrime(n)    