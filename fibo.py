def fibo(x):
	fib = list(range(x + 1))
	fib[0] = 0
	fib[1] = 1

	for i in range(2, x + 1): fib[i] = fib[i - 1] + fib[i - 2]
	
	return fib[x]

print(fibo(10))		