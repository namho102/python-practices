one_is_less_than_two = 1 < 2
print(one_is_less_than_two) #True

x = None
print(x is None)

all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list
any([]) # False, no truthy elements in the list