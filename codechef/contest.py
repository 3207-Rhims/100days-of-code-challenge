N=int(input())
count=0
if 1<= N <= 100000:
    for i in range(N*2+2):
        def isPrime(i): 
            if (i <= 1): 
                return False
            for j in range(2, i): 
                if (i % i == 0): 
                    return False
            return True
    if isPrime(i): 
        print (i) 
    else: 
        print ("false")    
  
