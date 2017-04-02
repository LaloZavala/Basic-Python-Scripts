
lista = []
for x in range(1,3,1):
	for y in range(1,4,1):
		a = input("a["+str(x)+"]["+str(y)+"] = ")
		b = int(a)
		lista.append(b)

delta = lista[0] * lista[4] - lista[1] * lista[3]

deltax = lista[2] * lista[4] - lista[1] * lista[5]

deltay = lista[0] * lista[5] - lista[3] * lista[2]

x = deltax/delta

y = deltay/delta

print("The results are: x = " + str(x)+ " and y = " + str(y))