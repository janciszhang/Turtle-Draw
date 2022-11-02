# -*- coding: utf-8 -*-

"""
没写出来！！！
"""
"""
分形树 fractal tree
递归
深度递归
"""

import turtle
import random


# 画树干
def paint_tree_trunk():
    p.pensize(thick)
    p.penup()
    p.left(90)
    p.forward(-length)
    p.pendown()
    p.forward(length)


# 画树枝（我没写出来）
def paint_fractal_tree(length, thick, check):
    if length < 30:
        return
    else:
        thick = thick * 3 / 4
        p.pensize(thick)
        length = length * 3 / 4

        # left
        if check == 0:
            p.left(45)
            p.forward(length)
            p.penup()
            p.backward(length)
            p.right(45)
            p.pendown()
            paint_fractal_tree(length * 4 / 3, thick * 4 / 3, 1)
            # paint_fractal_tree(length, thick, 0)

        # right
        else:
            p.right(45)
            p.forward(length)
            p.penup()
            p.backward(length)
            p.left(90)
            p.forward(length)
            p.pendown()
            paint_fractal_tree(length, thick, 0)


# 深度递归
def draw_tree(length, lv):
    length = length * 3 / 4
    thick = p.pensize()
    p.pensize(thick * 3 / 4)

    global r, g, b
    r += 1
    g += 2
    b += 3
    p.pencolor(r % 200, g % 200, b % 200)

    # left
    p.left(45)
    p.forward(length)
    if lv < 10:
        draw_tree(length, lv + 1)
    p.backward(length)
    p.right(90)

    # right
    p.forward(length)
    if lv < 10:
        draw_tree(length, lv + 1)
    p.backward(length)
    p.left(45)
    p.pensize(thick)


p = turtle.Turtle()
turtle.colormode(255)
p.speed(0)

length = 200
thick = 14
check = 0
r = 0
g = 0
b = 0

# turtle.tracer(False)
paint_tree_trunk()  # 画树干
draw_tree(length, 1)  # 画树枝
# paint_fractal_tree(length, thick, check)

# turtle.tracer(True)
turtle.done()
