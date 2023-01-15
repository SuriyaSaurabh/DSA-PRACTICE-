#question 5
# def csd(a):
# 	if a>2:
# 		csd(a-1)
# 		print("hello")
# 	print(a+5)

# csd(6)



#TYPE 1
# def M(a):
# 	print(a)
# 	if a>2:
#  		M(a-1)
#  		print("hello")
#  		print(a+5)
# M(6)


#type 2
def M(a):
	print(a)
	if 9>a>1:
		M(a+1)
		print("RAM")
	print(a+6)

M(2)