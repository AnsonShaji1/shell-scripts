import os
import sys
a='|--'
b=' |    '
c='\--'
x=0



def dirtree(dir,x):
	f=os.listdir(dir)


	p=f[-1]
	for i in f:
		if not os.path.isdir(dir+'/'+i):
			if i==p:
				print b*x,c,i
			else:
				print b*x,a,i
		else:
			print b*x+' '+a,i
			dir=dir+'/'+i
			dirtree(dir,x+1)
dirtree(sys.argv[1],x)
