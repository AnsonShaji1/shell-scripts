import sys
def head(a):
	f=open(a)
	b=f.readlines()
	c=[]
	print('head command......\n')
	for i in range(10):
		c.append(b[i].strip())
	
	for i in c:
		print i
		
print head(sys.argv[1])



def tail(a):
	f=open(a)
	b=f.readlines()
	c=b[::-1]
	d=[]
	print('\n\nTail command.....\n')
	for i in range(10):
		d.append(c[i].strip())
	
	for i in d:
		print i

print tail(sys.argv[1])

