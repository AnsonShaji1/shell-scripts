import sys
import os
d=[]
f=os.listdir(sys.argv[1])
for i in f:
	g=open(i)
	b=g.read()
	c=len(b)
	d.append(c)

a=zip(f,d)
for i in a:
	print i[0],'  ', i[1]
	

import sys
import os
def st(dir):
	f=os.listdir(sys.argv[1])
	for i in f:
		print i,len(open(os.path.abspath(sys.argv[1]+'/'+i)).read()),os.stat(os.path.abspath(sys.argv[1]+'/'+i))
st(sys.argv[1])
