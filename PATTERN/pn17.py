#type 1
n=5
for i in range(1,n+1):
	print(" "*(i-1),end="")
	for j in range(1,(2*n-2*i+2)):
		if j==1 or j==2*n-2*i+1:
			print("*",end="")
		else:
			print("_",end="")
	print()

#type 2
n=5
for i in range(n,0,-1):
	print(" "*(n-i),end=" ")
	for j in range(1,2*i):
		if j==1 or j==2*i-1:
			print("*",end="")
		else:
			print("_",end="")
	print()

