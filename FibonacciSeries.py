fibonacci_cache = {}

top = input("Number limit to the series:")
top = int(top)

def fibonacci(n):

	#if the n value has been already cached, then it is returned
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	#compute the nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	#the value is stored in the cache and then returned
	fibonacci_cache[n] = value
	return value

#prints the value until the number given - 1
for n in range(1, top):
	print(n, ";", fibonacci(n))