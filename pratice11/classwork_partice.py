# def factorial(n):
# 	result=1
# 	for i in range(2,n+1):
# 		result=result*i

# 	return result

# n=int(input("enter number: "))
# result=factorial(n)
# print(result)
#======================================================
# combination 

# def factorial(n):
# 	result=1
# 	for i in range(2,n+1):
# 		result=result*i

# 	return result

# def combination(n,r):
# 	result=factorial(n)//(factorial(r)*factorial(n-r))
# 	print(result)


# n=int(input("enter value of n: "))
# r=int(input("enter value of r: "))

# combination(n,r)

#==================================================================

#pascal 
# def factorial(n):
# 	result=1
# 	for i in range(2,n+1):
# 		result=result*i
# 	return result
# def combination(n,r):
# 	result=factorial(n)//(factorial(r)*factorial(n-r))

# 	return result

# def pascal(n):
# 	for i in range(1,n+1):
# 		print(" "*(n-i),end=" ")
# 		for j in range(1,i+1):
# 			comb=combination(i-1,j-1)
# 			print(comb,end=" ")
# 		print()

# n=int(input('enter number: '))
# pascal(n)

#=======================================================================
# n=43544
# count=0			o(n)
# while n>0:
# 	count=count+1
# 	n=n//10

# print(count)

# n=78956425652   #int me number deya 		O(n)
# k=str(n)  # string me covert keya 
# print(k)
# p=len(k) #string pe len function use kr ke counting kr le 
# print(p)

#======================================================
#n=435625
# sum=0
# while n>0:			# t.c=O(n)

# 	ld=n%10
# 	n=n//10
# 	sum=sum+ld
	
# print(sum)

# #use for loop

# n="435625"  #sting me convert kr ke kra deya 
# sum=0
# for ele in n:				#O(n)=t.c
# 	sum=sum+int(ele)

# print(sum)

#=================================================================
# to find armstrong number

# def digits(n):
# 	count=0
# 	while n>0:
# 		count=count+1
# 		n=n//10
# 	return count

# def power(a,b):
	
# 	result=1
# 	for ele in (1,b+1):

# 		result=result*a

# 	return result

# def amrstrong(self):
# 	d=digits(n)
# 	n1=n
# 	sum=0
# 	while n>0:
# 		ld=n%10
# 		sum=sum+power(ld,d)
# 		n=n//10
# 	if sum==n1:
# 		True
# 	else:
# 		False
	
# n=int(input('enter number: '))
# result=amrstrong(n)
# print(result)

#==========================================================================
#jo ek element apne right or left se bda hoga vo nekal ke dena h 
# def peak_element(arr):
#     l=len(arr)-1
#     for i in range(1,l):
#         if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#             return arr[i]
#     return -1



# #arr=[4,7,8,9,6,14]
# arr=[4,7,8,9,11,14]
# result=peak_element(arr)
# print(result)



#more than ek element apne right or left se bda hoga vo nekal ke dena h 
# def peak_element(arr):      
#     l=len(arr)-1
#     l1=[]
    
#     for i in range(1,l):
#     	flag=0
#     	if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
#             l1.append(arr[i])
#             flag=1

#     if flag==1:
#     	return l1


#     return -1



# arr=[4,7,8,9,6,8,5,14,3]   #9 8 14
# #arr=[4,7,9,82,90,100]
# result=peak_element(arr)
# print(result)



















#===================================================================================
#find the greast right and left  element in the araary 
# def greast_rightandleft_element(arr):				#14,75
#     l=len(arr)-1
#     for i in range(1,l):
#         if arr[i]>arr[i-1] and arr[i]<arr[i+1]:
#         	print(arr[i])

       
#     return -1



# #arr=[4,8,6,14,15,75,76,23,14]
# arr=[4,7,8,9,11,14]             #7,8,9,11

# #arr=[2,14,12,15,23,25,20,14,45,63]  #15,23,45
# # result=greast_rightandleft_element(arr)
# # print(result)
# greast_rightandleft_element(arr)


























#====================================================================================
#reverse print list/array 
#normal logic 

#doubt

# def reverse(arr):				
# 	arr1=arr[::]#colning
	
# 	n=len(arr1)
# 	j=0
# 	for i in range(n-1,-1,-1):
		
# 			arr[i]=arr1[j]  #replace ho rha h 
# 			j=j+1

		

# arr=[4,2,7,8,5]
# print(arr)
# reverse(arr)
# print(arr)

# result=reverse(arr)
# print(result)


# #sir ka ans 
# def rev(arr1):
# 	arr2=[]
# 	for ele in arr1[::-1]:
# 		arr2.append(ele)
# 		#print(arr2)
# 	for i in range(0,len(arr1)):
# 		arr[i]=arr2[i]


# arr=[4,2,7,8,5]
# print(arr)
# rev(arr)
# print(arr)


#doubt

#logic = swaping se 
# def reverse(arr):

# 	i=0
# 	j=len(arr)-1
# 	while(i<j):
# 		# c=arr[i]
# 		# arr[i]=arr[j]
# 		# arr[j]=c
# 		# i=i+1
# 		# j=j-1



# arr=[4,2,7,8,5]
# print(arr)
# # rev=reverse(arr)  #none kyu de rha h yha 
# # print(rev)
# reverse(arr)
# print(arr)



#current se next element ke sath swap kr rha h == left shifting
# def left_shift(arr):

# 	i=0
# 	j=len(arr)-1
# 	while(i<j):
		

# 		arr[i],arr[i+1]=arr[i+1],arr[i]  #doubt galat kyu aarha h ye 
# 		i=i+1
		
	
# arr=[4,2,7,8,5]
# print(arr)
# reverse(arr)
# print(arr)


#logic 1
# def reverse(arr):				O(n*2)

# 	i=0
# 	n=len(arr)-1
# 	for i in range(0,n):
# 		for j in range(i+1,n+1):
# 			arr[i],arr[j]=arr[j],arr[i]  #doubt galat kyu aarha h ye 

# 			#arr[4]arr[2]=arr[2]arr[4]
		
		
	
# arr=[4,2,7,8,5]
# print(arr)

# reverse(arr)
# print(arr)


#logic 2
# def reverse(arr):

# 	j=1
# 	n=len(arr)							#O(n)
# 	for i in range(0,(n//2)):
		
# 			arr[i],arr[n-j]=arr[n-j],arr[i]  #doubt galat kyu aarha h ye 
# 			j=j+1

# 			#arr[1]arr[2]=arr[2]arr[1]
		
		
	
# arr=[4,2,7,8,5]
# #arr=[4,5,6,4]
# print(arr)

# reverse(arr)
# print(arr)














#=================================================================================
#power nekal na 

# def power(a,b):
# 	result=1
# 	for i in range(1,b+1):
# 		result=result*a

# 	return result

# a=int(input('enter firt number:'))
# b=int(input('enter second number:'))
# result=power(a,b)
# print(result)

#===========================================
#check number of digits and how many number in a digits 
#use while loop

# def count_digits(n):
#  	count=0
#  	while n>0:
#  		count=count+1
#  		n=n//10
#  		#print(n)

#  	return count


# n=int(input('enter any number: '))
# count=count_digits(n)
# print(count)

#use for loop 
# def count_digits(n):
#  	value=n
#  	a=str(n)

#  	count=0
#  	for i in range(0,len(a)):
#  		count=count+1
#  		value=value//10
#  		#print(value)
#  	return count


# n=int(input('enter any number: '))
# count=count_digits(n)
# print(count)

#====================================================================
#find number of digits sum which pass by user 
#use while loop

# def sum_digits(n):
# 	sum=0
# 	while n>0:
	
# 		ld=n%10
# 		sum=sum+ld
# 		n=n//10

# 	return sum


# n=int(input('enter any number: '))
# result=sum_digits(n)
# print(result)



#use for loop 
# def sum_digits(n):			#doubt ye do ba chal rha h why 
# 	sum=0
# 	a=str(n)

# 	for i in range(0,len(a)):
# 		ld=n%10
# 		n=n//10
# 		sum=sum+ld
# 		#print(sum)


# 	#return sum
# 	print(sum)


# n=int(input('enter any number: '))
# sum_digits(n)

#result=sum_digits(n)
#print(result)

#======================================================================================


