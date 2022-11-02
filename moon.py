# -*- coding: utf-8 -*-

"""
moon and stars
"""

__author__ = '31370055 Jingmin Zhang'
__version__ = '3.8.5'
__create__ = '2021-09-21 12:04 AM'
__modify__ = '2021-09-21 12:04 AM'

from turtle import *
from random import random,randint
screen = Screen()
width,height = 800,600
screen.setup(width,height)
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)#这里要设为0，否则很卡
t = Turtle(visible = False,shape='circle')
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width/2,randint(-height/2,height/2))
stars = []
for i in range(200):
    star = t.clone()
    s =random() /3
    star.shapesize(s,s)
    star.speed(int(s*20))
    star.setx(width/2 + randint(1,width))
    star.sety( randint(-height/2,height/2))
    star.showturtle()
    stars.append(star)
while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor()<-width/2:
            star.hideturtle()
            star.setx(width/2 + randint(1,width))
            star.sety( randint(-height/2,height/2))
            star.showturtle()
            bgpic(r'moon.png')#随便下载一个月亮png文件
done()
