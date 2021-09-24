n=int(input('enter the number'))
num=1
pc=0
while pc<n:
	i=1
	sum=0
	while i<num:
		if num%i==0:
			sum=sum+i
		i=i+1
	if num==sum:
		print(num,'perfect')
		pc=pc+1
	num=num+1