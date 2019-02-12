# user=str(raw_input('pless not use (z)/Enter the any name >'))
# sum_1=''
# c=[]
# c=list(user)
# # print c
# A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
# for i in c:
# 	if i in A:
# 		num=A.index(i)
# 		s=num+1
# 		sum_1=sum_1+A[s]
# print sum_1
# join=''
# for j in sum_1:
# 	if j=='a':
# 		join=join+'A'
# 		continue
# 	elif j=='e':
# 		join=join+'E'
# 		continue
# 	elif j=='i':
# 		join=join+'I'
# 		continue
# 	elif j=='o':
# 		join=join+'O'
# 		continue
# 	elif j=='u':
# 		join=join+'U'
# 		continue
# 	join=join+j
# print join

# ye cod p alphabet print karta hai

# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);

# z=65
# for i in range(65,91):
# 	print z,chr(i)
# 	z+=1

#-------------------------------------------------------------------------------------------------------


# import string
# hi=[]
# while True:
# 	l=''
# 	a=string.ascii_lowercase
# 	z=list(a)
# 	print a
# 	user=str(raw_input('Enter the whords >'))
# 	hi=hi+list(user)
# 	for i in hi:
# 		if i in a:
# 			z.remove(i)
# 	print '--'
# 	for j in z:
# 		l=l+j
# 	print l