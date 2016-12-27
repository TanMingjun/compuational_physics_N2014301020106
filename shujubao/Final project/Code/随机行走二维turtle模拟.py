# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:13:56 2016

@author: TanMingjun
"""
import random
import turtle
wn=turtle.Screen()
wn.bgcolor('lightgreen')
tess=turtle.Turtle()
tess.color('hotpink')
tess.pensize(1)
for d in range (101):
    x=random.randrange(0,51)
    prob = random.random()
    tess.forward(x)
    tess.left(prob*360)
    tess.stamp()
wn.exitonclick()