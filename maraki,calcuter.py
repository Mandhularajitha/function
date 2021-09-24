def calculater(n1,n2,operator):
    if operator=="+":
        add=(n1+n2)
        return add
    elif operator=="-":
        sub=(n1-n2) 
        return sub
    elif operator=="*":
        mul=(n1*n2)
        return mul
    elif operator=="%":
        div=(n1%n2)
        return div
   

n1=int(input("enter num"))
n2=int(input("enter num"))
print(calculater(n1,n2,"+"))
print(calculater(n1,n2,"-"))
print(calculater(n1,n2,"*"))
print(calculater(n1,n2,"%"))
                  