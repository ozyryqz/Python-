#-*-coding:utf-8-*-
# x[i]特征
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3,4, 5, 6])
y = np.array([15, 19, 22, 27, 30, 31])
plt.scatter(x,y)
#plt.scatter(x,y,color ="red")
plt.show()
print (len(x))
print (len(y))

epsilon = 0.0001

alpha = 0.001
max_itor = 100000
diff = [0, 0]
error_one = 0
error_two = 0
m = len(x)
# 记录迭代次数
cont = 0

# 初始化参数
theta0 = 0
theta1 = 0

def model_fun(theta0, theta1, x0):
    h = theta0 + theta1*x0
    return h

while cont < max_itor:
    cont += 1
    for i in range(m):
        diff[0] = model_fun(theta0, theta1, x[i]) - y[i]
        theta0 -= alpha * diff[0]
        theta1 -= alpha * diff[0] * x[i]
    error_one = 0
    for i in range(m):
        error_one += (model_fun(theta0, theta1, x[i]) - y[i]) ** 2 / 2 * m
    if abs(error_one - error_two) < epsilon:
        break
    error_two = error_one
    print (theta0, theta1)
print (theta0, theta1)
# 12.0961685897 3.39114086225
print("迭代次数为%s"%cont)
