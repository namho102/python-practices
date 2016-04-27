def double(x): return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
print(twice_xs)
twice_xs = map(double, xs) # same as above
print(list(twice_xs))

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
print(list(products))

def is_even(x): return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above


# x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
