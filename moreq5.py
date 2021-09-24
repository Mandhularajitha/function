def fname(s):
    i=0
    x=[]
    while i<len(n):
        if n[i] not in x:
            x.append(n[i])
        i=i+1
    print(x)    
n=["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
fname(n)