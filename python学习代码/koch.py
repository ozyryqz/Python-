# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:57:15 2018

@author: Administrator
"""

#KochDrawV1.py
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    #level = 3 #3阶科赫曲线
    koch(400,3)
    turtle.right(120)
    koch(400,3)
    turtle.right(120)
    koch(400,3)
    turtle.hideturtle()
main()
