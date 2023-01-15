n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="") # 1 space deya h yha pe
	print("* "*(i),end="") # 1star with 1 space 
	print()
print()


n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="")  #1 space deya h
	for j in range(1,i+1):
		print("* ",end="")
	print()
print()



n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="")  #1 space deya h
	num=6
	for j in range(1,i+1):
		print(num,end=" ")  #1 space deya h 
	print()
print()


n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="")  #1 space deya h
	num=6
	for j in range(1,i+1):
		print(num,end=" ")  #1 space deya h 
		num=+1
	print()
print()

n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="")  #1 space deya h
	num=6
	for j in range(1,i+1):
		print(num,end=" ")  #1 space deya h 
		num=num+1
	print()
print()


n=5
for i in range(n,0,-1):
	print(" "*(n-i),end="")  #1 space deya h
	num=5
	for j in range(1,i+1):
		print(num,end=" ")  #1 space deya  h 
		num=num-1
	print()
print()