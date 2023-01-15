n=5
for i in range(n,0,-1):
	print(" "*(n-i),end=" ") # 1 space deya h yha pe
	print("*"*(i),end="")
	print()
print()


n=5
for i in range(n,0,-1):
	print("  "*(n-i),end=" ") #2 space deya yha pe 
	for j in range(1,i+1):
		print("* ",end="")
	print()
print()


n=5
for i in range(n,0,-1):
	print("  "*(n-i),end=" ") #2 space deya yha pe 
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
	print()	
print()


n=5
for i in range(n,0,-1):
	print("  "*(n-i),end=" ") #2 space deya yha pe 
	num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()	
print()


n=5
for i in range(n,0,-1):
	print("  "*(n-i),end=" ") #2 space deya yha pe 
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()	
print()

n=5
for i in range(n,0,-1):
	print("  "*(n-i),end=" ") #2 space deya yha pe 
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=+1
	print()	
print()