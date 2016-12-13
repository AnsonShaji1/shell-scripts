def cumulative_product(a):
	b=[]
	m=1
	for i in a:
		m *=i
		b.append(m)

	return b

print cumulative_product([1,2,3,4])
