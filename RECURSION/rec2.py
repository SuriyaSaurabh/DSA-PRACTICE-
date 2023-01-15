#ye mene keya trace
def f1(n):
	x=1
	if n>5:
		f1(n-1)
		x=x+1
	print(n)
	print(x)

f1(10)
