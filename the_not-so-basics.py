# Sorting

x = [48, 17, 25, 30]
y = sorted(x) # is [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

print(x)

# List Comprehensions

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
squares = [x * x for x in range(7)]
print(squares)
even_squares = [x * x for x in even_numbers]
print(even_squares)

import random
print(random.randrange(100))
print(random.randrange(3, 60))

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

