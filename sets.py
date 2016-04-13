# 'set' represents a collection of distinct elements

s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is still { 1, 2 }
print(s)
x = len(s) # equals 2
y = 2 in s # equals True
z = 3 in s # equals False