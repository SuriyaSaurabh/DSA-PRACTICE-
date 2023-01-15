#question 7 
# def csd(n,x):
# 	if n>1:
# 		x=x+2
# 		return csd(n-1,5)+n+x

# 	else:
# 		return 25
# result=csd(4,7)
# print(result)


#type 1
# def Q(n,x):
# 	if n<6:
# 		x=x+3
# 		return Q(n+1,5)+n+x

# 	else:
# 		return 25
# result=Q(2,7)
# print(result)


#type 2
def M(n,x):
	if 6<=n<18:
		x=x+4
		return M(n+1,6)+n+x
	else:
		return 30

result=M(6,8)
print(result)