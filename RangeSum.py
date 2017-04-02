start = input("Write the first number of the range: ")
end = input("write the last number of the range: ")

start, end = int(start), int(end)

acum = 0

for x in range(start, end + 1, 1):
	acum = acum + x

print("The total sum from " + str(start) + " to " + str(end) + " is: " + str(acum))