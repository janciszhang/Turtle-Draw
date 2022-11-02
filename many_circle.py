# -*- coding: utf-8 -*-

"""
画很多圈demo
画螺旋变色圈（两种方法：loop、递归）

画一个矩形（围绕原点） -> 画螺旋变色矩形
"""

import turtle
import random

# # 画圈demo
# p = turtle.Turtle()
# p.speed(0)
# for i in range(100):
#     p.circle(100)
#     p.right(17)
# turtle.done()

# 画螺旋变色圈 (loop)
def paint_many_circle1(p, r):
    while r < 200:
        p.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        p.circle(r)
        p.left(2)
        r += 1


# 画螺旋变色圈 (递归)
def paint_many_circle2(p, r):
    if r > 200:
        return
    else:
        p.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        p.circle(r)
        p.left(2)
        paint_many_circle2(p, r + 1)


# p = turtle.Turtle()
# turtle.colormode(255)
# p.speed(0)
# paint_many_circle1(p, 50)
# paint_many_circle2(p, 50)
# turtle.done()


# 画一个矩形（围绕原点）
def paint_rectangle(a,b):
    p.penup()
    p.right(90)
    p.forward(b / 2)
    p.left(90)
    p.forward(-a / 2)
    p.pendown()
    for i in range(2):
        p.forward(a)
        p.left(90)
        p.forward(b)
        p.left(90)

# 画螺旋变色矩形
def paint_many_rectangle(a,b):
    if a > 300:
        return
    else:
        p.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        paint_rectangle(a,b)
        p.penup()
        p.goto(0,0)
        p.left(2)
        paint_many_rectangle(a+1,b+1)

p = turtle.Turtle()
turtle.colormode(255)
p.speed(0)
# turtle.tracer(False)  # 不追踪小乌龟，可直接生成最终图案，而不是一笔一笔画！！！
paint_many_rectangle(50, 30)
# turtle.tracer(True)
turtle.done()

