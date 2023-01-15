#nomal kaju kali 

n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	for j in range(i):
		print("* ",end="")
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	for j in range(i):
		print("* ",end="")
	print()

#================================================================================
n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	num=1
	for j in range(i):
		print(num,end=" ")
		num=num+1
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	num=1
	for j in range(i):
		print(num,end=" ")
		num=num+1
	print()
print()
#===============================================================
n=5
for i in range(1,n+1):
	print(" "*(n-i),end="")
	num=5
	for j in range(i):
		print(num,end=" ")
		num=num-1
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end="")
	num=5
	for j in range(i):
		print(num,end=" ")
		num=num-1
	print()











