line=input().split(" ")
n,k=line
n=int(n)
k=int(k)
count=0
if k<=10**7 and n<=10**9:
    for i in range(n):
        t=int(input())
        if t%k==0:
            count=count+1
    print(count)