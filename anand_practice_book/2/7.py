
def min_num(a):
	mini=a[0]
	for i in a:
		for j in a:
			if i > j and j < mini:
				mini=j
				#print('if min j=',j,(i,j))
			elif i < j and i < mini: 
				mini=i
				#print ('else min i=',i,(i,j)) 
			elif((i == j) and (i < mini)):
				mini=i
				#print('min=',i,(i,j))
			else:
				#print('i>min and (i,j,min)',min,(i,j,min))
				continue

	return mini

print 'minimum number in a list=',min_num([5,8,2,56,8,1,10,45])


def max_num(a):
	maxi=a[0]
	for i in a:
		for j in a:
			if i > j and i > maxi:
				maxi=i
				#print('if min j=',j,(i,j))
			elif i < j and j > maxi: 
				maxi=j
				#print ('else min i=',i,(i,j)) 
			elif((i == j) and (i > maxi)):
				maxi=i
				#print('min=',i,(i,j))
			else:
				#print('i>min and (i,j,min)',min,(i,j,min))
				continue

	return maxi

print 'maximum number in a list=',max_num([5,8,2,8,78,1,10,45])

