n = int (input("请输入你想求和的范围（正负交错）："))
s = 0
for i in range(1,n):
    if i % 2 == 0:
        s = s - i
    elif i % 2 == 1:
        s = s + i
print(s)