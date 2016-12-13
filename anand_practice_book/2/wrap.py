import sys
f=open(sys.argv[1])
b=f.readlines()
print 'b=',b
c=''
d=[]
for i in range(len(b)):
	for j in range(len(b[i])):
		c=c+b[i][j]
		#print c
		h=len(c)
		#print 'length',h
		
		if int(sys.argv[2]) == h:
			d.append(c.strip())
			c=''
			#c=c+'\n'
			#print('hello')
	d.append(c.strip())
	c=''
		


for i in d:
	print i

