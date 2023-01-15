n=5
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i-j+1,end=" ")
		
	print()


n=5
for i in range(1,n+1):
	num=i
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
		
	print()
