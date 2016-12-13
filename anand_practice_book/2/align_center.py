import sys
f=open(sys.argv[1])
b=f.readlines()
c=len(max(b))
for i in b:
	p=(c-len(i))/2
	print ' '*p+i.strip()
