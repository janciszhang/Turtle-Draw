# -*- coding: utf-8 -*-

import turtle
import random


def paint_n_star(p, a, n):
    if n % 2 == 1:
        for i in range(n):
            p.forward(a)
            p.right(180 - 180 / n)

    else:
        print('Cannot paint even star')


def paint_star_sky(amount, start_n=[5]):
    for i in range(amount):
        p.penup()
        p.goto(random.randint(-630, 620), random.randint(-360, 370))
        p.pendown()
        color_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        p.color(color_rgb)
        p.fillcolor(color_rgb)
        p.begin_fill()
        paint_n_star(p, 20, random.choice(start_n))
        p.end_fill()


turtle.bgcolor('black')
turtle.setup(1314, 800, 200, 200)
p = turtle.Turtle()
turtle.colormode(255)
start_n = [5, 7, 9, 11]
# turtle.tracer(False)
paint_star_sky(520, start_n)
# turtle.tracer(True)
turtle.done()
