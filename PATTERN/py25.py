n=7
for i in range(n,0,-1):
	for j in range(1,2*n+1):
		if j<=(n-i+1) or j>=(n+i):

			print("* ",end="")

		else:
			print("  ",end="")
	print()
for i in range(1,n+1):
	for j in range(1,2*n+1):
		if j<=(n-i+1) or j>=(n+i):

			print("* ",end="")

		else:
			print("  ",end="")
	print()
