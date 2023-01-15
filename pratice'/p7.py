#odd kaju katli 1,3,5,7,9

n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	for j in range(1,2*i):
		print("*",end="")
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	for j in range(1,2*i):
		print("*",end="")
	print()
print()

#======================================================================
n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	num=1
	for j in range(1,2*i):
		print(num,end="")
		num=num+1
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	num=1
	for j in range(1,2*i):
		print(num,end="")
		num=num+1
	print()
print()

#====================================================================
n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	num=9
	for j in range(1,2*i):
		print(num,end="")
		num=num-1
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	num=9
	for j in range(1,2*i):
		print(num,end="")
		num=num-1
	print()
print()