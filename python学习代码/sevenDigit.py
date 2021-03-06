# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:36:42 2018

@author: Administrator
"""

#绘制数码管
import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
#绘制单段数码管
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
#根据数字绘制数码管
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
#为绘制后续数码管确定位置
    turtle.penup()
    turtle.fd(20)
def drawDate(date):#data为日期，格式为‘%y-%m=%d+’
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial",26,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial",26,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write("日",font=("Arial",26,"normal"))
        else:
            drawDigit(eval(i))
def main ():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
