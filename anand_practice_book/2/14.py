def unique(a,key=lambda x: x.lower()):
	b=[]
	for i in a:
		if key(i) not in b:
			b.append(key(i))
	return b
		
	
print unique(['Anson','python','java','Python','Java'],key=lambda x: x.lower())
