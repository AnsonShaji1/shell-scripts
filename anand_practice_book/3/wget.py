import sys
import urllib

list=sys.argv[1].split('/')
a=urllib.urlopen(sys.argv[1])
b=a.read()


if list[-1] == '':
	f=open('index.html','w')
	f.write(b)
	f.close()
else:
	f=open(list[-1],'w')
	f.write(b)
	f.close()




