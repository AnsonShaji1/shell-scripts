def cumulative_sum(a):
	b=[]
	m=0
	for i in a:
		m +=i
		b.append(m)

	return b

print cumulative_sum([1,2,3,4])
	
