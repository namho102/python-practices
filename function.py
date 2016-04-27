def double(x):
	return x * 2

print(double(15))

def apply_to_one(f):
	return f(3)

my_double = double
x = apply_to_one(double)

print(x)

def my_print(message="my default message"):
	print(message)		

my_print()

# print for fun
print(my_print)

def print_info( name, age = 35 ):
   print("Name: ", name)
   print("Age: ", age)
   
print_info('Leo');


def printinfo( arg1, *vartuple):
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)

printinfo( 10 )
printinfo( 70, 60, 50 )   