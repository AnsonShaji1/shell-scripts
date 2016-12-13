f=open('she.txt')
a=f.readlines()
b=[]
e=''
for i in a:
	x=i.split()
	y=x[::-1]
	b.append(y)


for i in range(len(b)):
	for j in range(len(b[i])):
		c=b[i][j]
		d=c[::-1]
		e=e+d+' '
	print e


				

	
