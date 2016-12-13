def factorial(a):
	sum=1
	for i in range(a+1):
		if i == 0:
			continue
		sum *=i
	return sum

print factorial(1)
