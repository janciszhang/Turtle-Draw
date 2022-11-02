# -*- coding: utf-8 -*-

import turtle

# 彩色螺旋线（绕原点螺旋正方形）
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow", "purple", "blue"]
turtle.speed(0)
# turtle.tracer(False)  # 不追踪小乌龟，可直接生成最终图案，而不是一笔一笔画！！！
for x in range(400):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)
# turtle.tracer(True)
turtle.done()
