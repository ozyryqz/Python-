first = 1
second = 1
n = 2
print ("Please input a number :")
num = int ( input("n :") )
if num == 0:
    print("This input is wrong !")
elif num == 1 :
    print(first)
elif num == 2 :
    print(first)
    print(second)
elif num > 2 :
    third = second + first 
    print(first)
    print(second)
while n < num :
    print(third)
    first = second
    second = third
    third = second + first
    n += 1
