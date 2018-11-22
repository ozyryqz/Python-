# -*-coding:utf-8-*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
# 采样
x = np.array([1, 2, 3,4, 5, 6])
y = np.array([15, 19, 22, 27, 30, 31])
# 画出散点图
plt.scatter(x,y)

# 假设函数
def func_least(p,x):
    k,b =p
    y = k*x+b
    return y
# 代价函数
def cost_func(p,x,y):
    return func_least(p,x)-y
# 假设参数值
p = [100,50]
# 最小二乘法
pa = leastsq(cost_func,p,args=(x,y))
k,b =pa[0]

x= np.linspace(1,6,100)
y = k*x+b
plt.scatter(x,y,color ="red")
print (k,b)
# 3.3714285712178196 12.199999999917608
plt.show()
