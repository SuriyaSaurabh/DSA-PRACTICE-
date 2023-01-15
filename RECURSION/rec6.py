#question 6
# def S1(n):
# 	if n>1:
# 		return S1(n-1)+n

# 	else:
# 		return 5

# result=S1(4)
# print(result)


#type 1
# def M(n):
# 	if n>2:
# 		return M(n-1)+n
# 	else:
# 		return 5

# result=M(6)
# print(result)


#type 2
# def X(n):
# 	if 2<n>=3:
# 		return X(n-1)+n

# 	else:
# 		return 30

# result=X(8)
# print(result)



#type 3
# def X(n):
# 	if 9>n<=8:
# 		return X(n+1)+n

# 	else:
# 		return 30

# result=X(1)  
# print(result)


#type 4
def X(n):
	if 9>n>=8:
		return X(n+1)+n

	else:
		return 30

result=X(10.45)  
print(result)
