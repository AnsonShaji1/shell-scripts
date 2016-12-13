def unique(a,key=lambda x: x.lower()):
	b=set()
	for i in a:
		if key(i) not in b:
			b.add(key(i))
	return b
		
	
print unique({'python','java','Python','Java'},key=lambda x: x.lower())
