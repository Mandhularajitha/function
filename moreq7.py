n1 = [1, 5, 10, 12, 16, 20]
n2 = [1, 2, 10, 13, 16]
i=0
b=[]
while i<len(n1):
    j=0
    while j<len(n2):
        if n1[i]==n2[j]:
            b.append(n1[i])
        j=j+1
    i=i+1
print(b)




# def fname(n1,n2):
#     t=n1+n2
#     i=0
#     x=[]
#     while i<len(t):
#         if t[i] not in x:
#             x.append(t[i])
#         i=i+1
#     x.sort()
#     print(x)
# s = [1, 5, 10, 12, 16, 20]
# k = [1, 2, 10, 13, 16]
# fname(s,k)






# def fname(n1,n2):
#     i=0
#     j=0
#     b=[]
#     while i<len(n1)and j<len(n2):
#         if n1[i]!=n2[j]:
#             b.append(n1[i])
#             b.append(n2[j])
#         j=j+1
#         i=i+1
#     b.append(n1[i])
#     print(b)
# s = [1, 5, 10, 12, 16, 20]
# k = [1, 2, 10, 13, 16]
# fname(s,k)