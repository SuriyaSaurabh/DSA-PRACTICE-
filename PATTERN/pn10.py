n=5
for i in range(1,n+1):
	num=i
	print(" "*(i-1),end=" ")
	for j in range(1,n-i+2):
		print(num,end=" ")
		num=num+1
	print()
for i in range(n,0,-1):
	num=i
	print(" "*(i-1),end=" ")
	for j in range(1,n-i+2):
		print(num,end=" ")
		num=num+1
	print()
