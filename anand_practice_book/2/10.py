a=[1,2,1,3,2,5]
def unique(a):
	b=[]
	for i in a:
		if i in b:
			continue
		b.append(i)

	return b

print unique(a)
	
