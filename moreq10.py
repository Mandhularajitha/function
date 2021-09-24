m = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
i=0
b=[]
a=" "
while i<len(m):
	if m[i]==" ":
	    b.append(a)
	    a=" "
	else:
		a=a+m[i]
	i=i+1
b.append(a)
print(b)





