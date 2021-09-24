def fname(n):
    k=1
    while k<=n:
        j=k
        s=0
        while j>0:
            y=j%10
            s=s+y
            j=j//10
        if k%s==0:
            print(k)
        k=k+1
s=int(input("enter num"))         
fname(s)   

