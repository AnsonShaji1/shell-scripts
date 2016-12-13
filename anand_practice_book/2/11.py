a=[1,2,1,3,2,5,3,3,4,4,1]
def dups(a):
	b=[]
	c=[]
	for i in a:
		if i in b and i not in c:
			c.append(i)
		b.append(i)

	return c

print dups(a)
