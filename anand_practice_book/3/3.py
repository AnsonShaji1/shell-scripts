import sys
import os
def st(dir):
	f=os.listdir(sys.argv[1])
	for i in f:
		print i,len(open(sys.argv[1]+'/'+i).read()),os.stat(sys.argv[1]+'/'+i)[8]
st(sys.argv[1])
