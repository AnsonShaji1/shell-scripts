def extsort(a):
	b=[]
	h=[]
	for i in a:	
		d=i.split('.')[0]
		c=i.split('.')[1]
		b.append((d,c))

	b.sort(key=lambda x: x[1])

	for j in range(len(b)):
		n='.'.join(b[j])
		h.append(n)

	return h


a=['a.c','a.py','b.py','bar.txt','foo.txt','x.c']
print extsort(a)

