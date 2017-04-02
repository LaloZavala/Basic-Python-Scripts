table = input("Which multiplication table do you want to see?")

table = int(table)

for x in range(11):
	print(str(table) + " x " + str(x) + " = " + str(table*x))