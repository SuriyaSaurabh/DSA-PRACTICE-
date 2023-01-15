n=10
for i in range(1,n+1):
	for j in range (1,n-i+1):
		print(" ",end=" ")
	for k in range (1,i+1):
		print("*",end=" ")
		# print(j,end=" ")
	print()

#method2
n=5
for i in range(1,n+1):
	print(" "*(n-i),end=" ")
	print("*" * i)


n=5
for i in range(1,n+1):
	print('  '*(n-i),end=' ')
	for j in range(1,i+1):
	 	print("*",end=" ")
	print()