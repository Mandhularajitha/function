m = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i=0
max=0
s=[]
while i<len(m):
    j=0
    while j<len(m[j]):
        if m[i][j]>max:
            max=m[i][j]
        j=j+1   
    i=i+1
    print(max)            
