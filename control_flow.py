if 1 > 2:
	print('if only 1 were greater than 2')
elif 1 > 3:
	print("elif stands for 'else if'")
else:
	print("when all else fails use else (if you want to)")

x = 3
parity = "even" if x % 2 == 0 else "odd"
print(parity) #odd

x = 20
while x > 10:
	print(x, "is greater than 10")
	x -= 1

for x in range(10):
	print(x, "is less than 10")

for x in range(10):
	if x == 3:
		continue # go immediately to the next iteration
	if x == 5:
		break # quit the loop entirely
	print(x)					