t=int(input())
if  1<=t<=1000:
    for i in range(t):
        num=int(input())
        sum=0
        while num!=0:
            sum=sum+int(num%10)
            num=int(num/10)
        if 1<=num<=1000000:    
            print(sum) 
   
    