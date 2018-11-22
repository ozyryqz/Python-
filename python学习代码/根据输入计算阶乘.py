#计算给定输入的阶乘
#通过定义函数，调用函数实现
def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s
N = eval(input("请输入您要计算的数字："))
question = fact(N)
print("您计算的{}的阶乘为：".format(N),question)