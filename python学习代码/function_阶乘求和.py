N = int (input("Please input a number "))
s = 0
t = 1
for i in range(1,N):
    while i > 0 :
        t = t*i
        i = i -1
    s = s + t
    t = 1

print (s)
    
