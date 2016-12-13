def group(a,n):
	l=len(a)
	b=[]
	c=[]
	j =0
	for i in range(l):
		if(j < n-1):
			j += 1
			b.append(a[i])
		else:
			j = 0
			b.append(a[i])
			c.append(b)
			b= []
	if(b!= []):
		c.append(b)
	return c

print group([1,2,3,4,5,6,7,9,10,11],3)

	


