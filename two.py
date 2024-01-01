while(1):
	number = int(input("Enter a number: "))

	for count in range(1, 11):
		product = count * number
		print(number, "x", count, "=", product)