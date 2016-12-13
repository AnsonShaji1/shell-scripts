def words(a):
	f=open(a)
	b=f.read().split()
	return b

def count_words(b):
	f={}
	for i in b:
		f[i]=f.get(i,0) + 1
	return f

if __name__ == "__main__":
	import sys
	b=words(sys.argv[1])
	print b
	
	c=count_words(b)
	for i,j in c.items():
		print i,j
