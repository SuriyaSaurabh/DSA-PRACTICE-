#doubt
# n=5
# for i in range(1,n+1):
# 	for j in range(1,n+i):

# 		if i%2==1:
# 		    print(1,end='')
# 		else:
# 			i%2==0
# 			print(0,end='')
		
# 		print()

			
n=5
for i in range(1,n+1):
	for j in range (i,n+i):
		
		print(" ", end="")

	for k in range(i,i+5):
		if i%2==1:
		    print(1,end='')
		else:
			i%2==0
			print(0,end='')
		
		

	print()
print()