import sys
f=open(sys.argv[1])
b=f.readlines()
c=[]
for i in range(len(b)):
	if sys.argv[2] in b[i]:
		c.append(b[i].strip())
		

for i in c:
	print i
