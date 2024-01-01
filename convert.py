print("             ")
print("*****conveting Km to Miles*****")

print("             ")
num = int(input("enter 1 to convert or 0 to exit: "))
print("             ")

if num == 1:
	while(1):
		Km = float(input("Input kilometer: "))
		Miles = Km * 0.621371
		print(f"{Km} Kilometer is {Miles} Miles")
		print("             ")