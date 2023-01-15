n=5
m=10
a=1
for i in range(n,0,-1):
	
	for j in range(a,m):
	 	if j+i==6 or i-j== -4:
	 		print("*",end='')
	 	else:
	 		print(' ',end='')
	
	print()
for i in range(2,n+1):
	
	for j in range(a,m):
	 	if j+i==6 or i-j== -4:
	 		print("*",end='')
	 	else:
	 		print(' ',end='')
	
	print()