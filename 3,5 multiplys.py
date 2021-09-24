def fname(n):
    i=1
    sum=0
    while i<=n:
        if i%3==0 or i%5==0:
            sum=sum+i
            print("divisibles",i)
        i=i+1
    print("divisible sum",sum)
s=int(input("enter the user number"))
fname(s)        


