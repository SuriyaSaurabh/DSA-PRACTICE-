#blank kaju katli

n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	for j in range(1,i+1):
		if j==1 or j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
for i in range(n,0,-1):
	print(" "*(n-i),end="")
	for j in range(1,i+1):
		if j==1 or j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()




