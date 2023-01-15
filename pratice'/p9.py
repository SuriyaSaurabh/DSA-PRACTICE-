n=5
for i in range(1,n+1):
		print("* "*(i))
for i in range(n-1,0,-1):
		print("* "*(i))
print()


n=5
for i in range(1,n+1):
		print(n,end='')
		n=n+1
		print()
print()


#same
n=5
for i in range(1,n+1):
	for j in range(1,i+1):
	 	print("*",end=" ")
	print()
for i in range(n-1,0,-1):
	for j in range(1,i+1):
	 	print("*",end=" ")
	print()
#=========================================
#Q 2
n=5
for i in range(1,n+1):
	num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()
for i in range(n-1,0,-1):
	num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()
print()
#=======================================================
n=5
for i in range(1,n+1):
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()
for i in range(n-1,0,-1):
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()
print()
#======================================================

n=5
for i in range(1,n+1):
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()
for i in range(n-1,0,-1):
	num=5  #num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()
print()
#===============================================
n=5
for i in range(1,n+1):
	num=5
	for j in range(1,i+1):
		print(num,end=" ")
		num=num-1
	print()
for i in range(n-1,0,-1):
	num=1
	for j in range(1,i+1):
		print(num,end=" ")
		num=num+1
	print()