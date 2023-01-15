#downword triangle 
n=5
for i in range(1,n+1):
	for j in range (1,i+1):
		print(end=" ")
	for k in range (n+1,i,-1):
		print("*",end=" ")
	print()
print()
n=5
for i in range(1,n+1):
	for j in range (i+1):
		print(" ", end="")

	for k in range(n+1,i,-1):
		print("* ", end="")
	print()
print()

n=5
for i in range(n):
	for j in range (i):
		print("",end="")
	for k in range (n,i,-1):
		print("*",end=" ")
	# 	# print(j,end=" ")
	print()
print()