doubt
n=5
for i in range(1,n+1):
	print(" "*(n-i),end=" ")
	if i==1 or i==(2*i-1):
		print("*"*(2*i-1))
print()

for i in range(n-1,0,-1):
	print(" "*(n-i),end=" ")
	if i==1 or i==(2*i-1):
		print("*"*(2*i-1))
print()

