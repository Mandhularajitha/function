n1=[1, 342, 75, 23, 98]
n2=[75, 23, 98, 12, 78, 10, 1]
i=0
b=[]
while i<len(n1):
    j=0
    while j<len(n2):
        if n1[i]==n2[j]:
            b.append(n1[i])
        j=j+1
    i=i+1
b.sort()
print(b)