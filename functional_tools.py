def double(x): return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
print(twice_xs)
twice_xs = map(double, xs) # same as above
print(list(twice_xs))