import math
n = 0
largest_so_far = -math.inf
numbers = [3,14,1,-98,-8,0,4,-5]
for i in numbers:
    if i > largest_so_far :
        largest_so_far = i
        n += 1
print(largest_so_far)
print(n)
