num = 1234
n0 = num%10
num = int ( (num - n0)/10 )
n1 = num %10
num = int ( (num - n1)/ 10 )
n2 = num % 10
num = int ( ( num - n2 ) / 10 )
n3 = num % 10
print(n0,n1,n2,n3)
