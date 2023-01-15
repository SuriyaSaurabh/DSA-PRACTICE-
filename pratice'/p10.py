n=5
for i in range(1,n+1):         #space pe game khelo bs    
	print("  "*(n-i),end=' ')  # 2 space *(n-i)
	print("* "*(i))            #"* "*(i)   1 star 1space
for i in range(n-1,0,-1):         #space pe game khelo bs    
	print("  "*(n-i),end=' ')  # 2 space *(n-i)
	print("* "*(i))   
print()
#====================================================================
#same
n=5
for i in range(1,n+1):
	print("  "*(n-i),end=' ') #2 space 
	for j in range(1,i+1):
	 	print("* ",end="")  # 1 star or 1 space deya 
	print()
for i in range(n-1,0,-1):
	print("  "*(n-i),end=' ')
	for j in range(1,i+1):
	 	print("* ",end="")
	print()
print()


#====================================================================
n=5
for i in range(1,n+1):
	print(' '*(n-i),end=' ')
	for j in range(1,i+1):
	 	print("*",end="")
	print()	
for i in range(n-1,0,-1):
	print(' '*(n-i),end=' ')
	for j in range(1,i+1):
	 	print("*",end="")
	print()	



#====================================================================
n=5
for i in range(1,n+1):
	print('  '*(n-i),end=' ')
	num=1
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
for i in range(n-1,0,-1):
	print('  '*(n-i),end=' ')
	num=1
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
print()
#=================================================
n=5
for i in range(1,n+1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
for i in range(n-1,0,-1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
print()
#===========================================================
n=5
for i in range(1,n+1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
for i in range(n-1,0,-1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num-1
	print()	
print()
#===================================
n=5
for i in range(1,n+1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num-1
	print()	
for i in range(n-1,0,-1):
	print('  '*(n-i),end=' ')
	num=5
	for j in range(1,i+1):
	 	print(num,end=" ")
	 	num=num+1
	print()	
