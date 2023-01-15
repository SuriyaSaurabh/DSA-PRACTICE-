n=5
for i in range(1,n+1):
	print("  "*(n-i),end=" ")
	for j in range(1,2*i):
		if i%2==0:
			print("_",end=" ")
		else:
			print("*",end=" ")
	print()
for i in range(n-1,0,-1):
	print("  "*(n-i),end=" ")
	for j in range(1,2*i):
		if i%2==0:
			print("_",end=" ")
		else:
			print("*",end=" ")
	print()