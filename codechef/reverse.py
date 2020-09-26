t=int(input())

for i in range(t):
    n=int(input())
    r=0
    while n>0:
        rem=n%10
        r=(r*10)+rem
        n=int(n/10)
    print(r)
        
    