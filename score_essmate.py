# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:30:52 2018

@author: Administrator
"""

score = int(input("请输入成绩："))
if score <= 60:
    grade = 'D'
elif score <= 70:
    grade = 'C'
elif score <= 80:
    grade = 'B'
elif score <= 90:
    grade = 'A'
print("输出的成绩所在级别为:{}".format(grade))