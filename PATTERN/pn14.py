n=4
# track=0
for i in range(1,n+1):
	print(" "*(n-i),end=" ")
	num=i
	track=0
	for j in range(1,2*i):
		print(num,end="")
		# print("*",end="")
		if track==0:
			num=num-1
		else:
			num=num+1
		if num==1:
			track=1
	print()
for i in range(n-1,0,-1):
	print(" "*(n-i),end=" ")
	num=i
	track=0
	for j in range(1,2*i):
		print(num,end="")
		 #print("*",end="")
		if track==0:
			num=num-1
		else:
			num=num+1
		if num==1:
			track=1
	print()