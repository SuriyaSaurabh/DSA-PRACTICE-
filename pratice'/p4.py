n=5
for i in range(n,0,-1):
	print(""*(n-i),end=" ")  #space nhi dena 
	print("*"*(i),end="")
	print()
print()

n=5
for i in range(n,0,-1):
	print(""*(n-i),end="")  #space nhi dena 
	for j in range(1,i+1):
		print("* ",end="")
	print()
print()


n=5
for i in range(n,0,-1):
	print(""*(n-i),end="")
	num=3
	for j in range(1,i+1):
		print(num,end=" ")
	print()
print()


n=5
for i in range(n,0,-1):
	print(""*(n-i),end="")
	num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()


n=5
for i in range(n,0,-1):
	print(""*(n-i),end="")
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()
print()
n=5
for i in range(n,0,-1):
	print(""*(n-i),end="")
	num=7
	for j in range(1,i+1):
		print(num,end=" ")
		num=+1
	print()