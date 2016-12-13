import sys
import os

def extcount(dir):
	f=os.listdir(sys.argv[1])
	a=[]
	d={}
	for i in f:
		x=i.find('.')
		
		c=i[x+1:]
		
		a.append(c)
		

	for j in a:
		d[j]=d.get(j,0)+1

	for i,j in d.items():
		print i,j
extcount(sys.argv[1])
