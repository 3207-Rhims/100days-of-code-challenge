t=int(input())
for i in range(t):
    n=input()
    l=len(n)
    n=[str(c) for c in n]
    if l%2==0:
        p=int(l/2)
        #print(p)
        r=n[ :p]
        #print(r)
        s=n[p: ]
        #print(s)
        r.sort()
        s.sort()
        if r==s:
            print("YES")
        else:
            print("NO")    
    else:
        p=int(l/2)
        k=int(p+1)
        r=n[ :p]
        s=n[k: ]
        r.sort()
        s.sort()
        if r==s:
            print("YES")  
        else:
            print("NO")           