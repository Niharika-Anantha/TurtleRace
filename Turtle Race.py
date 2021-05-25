"""Basics of Turtle 

import turtle

s=turtle.getscreen()

t=turtle.Turtle()
turtle.bgcolor("blue")

turtle.title("My Game")

#Changing Turtle size
t.shapesize(3,3,3)#stretch length,stretch width,outline width
#Changing the color of the turtle
t.fillcolor("red")

#Changing pensize
t.pensize(5)
t.forward(100)
#Changing pen color
t.pencolor("green")

#moving the turtle
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.circle(60)

t.dot(20)"""

"""
t.begin_fill()
t.forward(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()
"""


"""
#Shape
#t.shape("turtle")
#t.shape("arrow")
#t.shape("circle")


#Speed
t.speed(1)
t.fd(100)
t.speed(10)
t.fd(100)


Customizing in one line


#Many Lines

t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(90)


Few Lines
t.pen(pencolor="purple",fillcolor="orange",pensize=10,speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
"""


"""
#Picking the pen up and down

t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()



t.undo()

#t.clear()

#t.reset()

Leaving a stamp
t.stamp()
t.fd(100)
t.stamp()
t.fd(100)



#t.clearstamp(8)


c=t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

"""

"""
for i in range(4):
    t.fd(100)
    t.rt(90)

"""

"""
n=10
while n<=40:
    t.circle(n)
    n+=10
    
"""

"""

u=input("Would you like me to draw a shape? Type yes or no: ")
if(u=="yes"):
    t.circle(100)
else:
    print("OK")
"""

"""

"""

import turtle
import random

player_one=turtle.Turtle()
player_one.color("green")

player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two=player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

die=[1,2,3,4,5,6]

for i in range(20):
    if player_one.pos()>=(300,100):
        print("Player one wins!")
        break
    elif player_two.pos()>=(300,-100):
        print("Player two wins!")
        break
    else:
        player_one_turn=input("Press 'Enter' to roll the die")
        die_outcome=random.choice(die)
        print("the result of the die roll is:")
        print(die_outcome)
        print("The number of steps will be:")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn=input("Press 'Enter' to roll the die")
        die_outcome=random.choice(die)
        print("the result of the die roll is:")
        print(die_outcome)
        print("The number of steps will be:")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)





































































































































