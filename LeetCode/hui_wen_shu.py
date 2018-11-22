print("Please input a five bit number")
n = int (input ( ))
t = n
n0 = n % 10
n = int ((n - n0)/10)
n1 = n % 10
n = int ((n - n1)/10)
n2 = n % 10
n = int ((n - n2)/10)
n3 = n % 10
n = int ((n - n3)/10)
n4 = n % 10
if n0 == n4:
    if n1 == n3:
        print("This number is a good number ",t)
elif n0 != n4:
    print("This number is a bad number")
