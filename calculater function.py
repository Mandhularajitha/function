def add(n1,n2):
    x1=n1+n2
    return x1
def sub(n1,n2):
    x2=n1-n2
    return x2
def mul(n1,n2):
    x3=n1*n2
    return x3
def div(n1,n2):
    x4=n1%n2
    return x4
def fname(a,b):
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))

n1=int(input("enter num"))
n2=int(input("enter num"))
fname(n1,n2) 
