def count_sum(n):
	a = 3
	b1 = 1
	sum_of_nums = 0
	for i in range(n):
		sum_of_nums += b1 + a * i

	return sum_of_nums

'''n = int(input("Enter count of numbers:"))
print(count_sum(n))'''