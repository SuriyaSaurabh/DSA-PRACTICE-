def f(m):
	print(m)
	if m<6:
		f(m+1)
	print(m+5)
f(1)


#type 1
def f(m):
	print(m)
	if m<6<8:
		f(m+1)
	print(m+5)
f(1)


#type 2
def f(m):
	print(m)
	if m<6>5:
		f(m+1)
	print(m+5)
f(1)

