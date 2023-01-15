n=5
for i in range(1,n+1):
	num=i%2
	for j in range(1,n+1):
		print(num,end=" ")
		# num=0 if num ==1 else 1
		
		if(num%2==0):
			num=1
		else:
			num=0
	print()