# -*- coding: utf-8 -*-

import turtle

# 设置turtle背景
# turtle.bgcolor('red')
turtle.bgpic("./比卡丘.png")
# 设置turtle窗口宽高w,h和初始位置x,y (同java setBound)
turtle.setup(600, 400, 0, 0)

# 设置画笔坐标
p = turtle.Turtle()
p.speed(2)  # 速度调到最快：0
p.pensize(20)  # 设置画笔的粗细
p.color('blue')  # 设置画线颜色
turtle.tracer(False)  # 追踪器，False-不追踪小乌龟，可直接生成最终图案，而不是一笔一笔画！！！
p.forward(200)
# 设置画笔坐标 - 回到原点(0, 0)
p.goto(0, 0)
# 给画出的图形填充颜色（设置填充颜色-> 开始填充 -> 画图 -> 结束填充）
turtle.colormode(255)  # 设置colormode为255，否则默认为0-1的小数
p.fillcolor(1, 200, 30)  # 要先设置colormode为255，否则默认为0-1的小数！！！
p.begin_fill()
p.circle(50)
p.end_fill()
turtle.tracer(True)
turtle.done()  # pycharm不加这行会闪退

# # turtle画图的抬笔、落笔
# p = turtle.Turtle()
# print(p) # 对象地址值
# p.forward(200) # 向前200
# p.left(90) # 左转90°
# # 抬笔
# p.penup()
# p.forward(200)
# # 落笔
# p.pendown()
# p.left(90)
# p.forward(200)
# turtle.done() # pycharm不加这行会闪退
