# -*- coding: utf-8 -*-

"""
random背景
画五角星 -> 画n角星
画星空
"""

import turtle
import random

# random背景
a = [1, 2, 3, 4, 5, 6]


# print(random.random())  # [0,1)
# print(a[random.randint(0, 5)])  # random.randint(a,b) -> [a,b] 左右端都包括!!!
# print(random.choice(a))  # random.choice(seq) 从非空序列取随机ele


# # 画五角星
# p = turtle.Turtle()
# for i in range(5):
#     p.forward(200)
#     p.right(144)
#
# turtle.done()


# 画n角星 (a为边长)
def paint_n_star(p, a, n):
    if n % 2 == 1:
        for i in range(n):
            p.forward(a)
            p.right(180 - 180 / n)

    else:
        print('Cannot paint even star')


# p = turtle.Turtle()
# paint_n_star(p, 200, 7)
# turtle.done()


# 画星空
def paint_star_sky(amount, start_n=[5]):
    for i in range(amount):
        p.penup()
        p.goto(random.randint(-480, 480), random.randint(-380, 380))
        p.pendown()
        color_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        p.color(color_rgb)
        p.fillcolor(color_rgb)
        p.begin_fill()
        paint_n_star(p, 20, random.choice(start_n))
        p.end_fill()


# turtle.bgpic("./比卡丘.png")
turtle.bgcolor('black')
turtle.setup(1000, 800, 0, 0)
p = turtle.Turtle()
turtle.colormode(255)
start_n = [5, 7, 9, 11]  # 必须为奇数
# 开始画
# turtle.tracer(False)
paint_star_sky(520, start_n)
# turtle.tracer(True)
turtle.done()
