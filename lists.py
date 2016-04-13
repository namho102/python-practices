integer_list = [1, 25, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

print(integer_list)
print(len(heterogeneous_list))
print(sum(integer_list))

x = range(10)

# first_three
print(x[:3])
# three_to_end
print(x[3:])
# one_to_four 
print(x[1:5])

print(1 in [1, 2, 3])

x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1,2,3,4,5,6]
print(x) 

x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6]; x is unchanged

x = [1, 2, 3]
x.append(0) # x is now [1, 2, 3, 0]

x, y = [1, 2] # now x is 1, y is 2

_, y = [1, 2] # now y == 2, didn't care about the first element
