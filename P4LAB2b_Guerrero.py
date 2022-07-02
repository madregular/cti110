# Turtle Graphics
# CTI-110
# 7/2/22
# Arturo Guerrero

#initialize
import turtle
win = turtle.Screen()

# make your turtle
arturtle = turtle.Turtle()
arturtle.color("red")
arturtle.shape("turtle")
arturtle.pensize(2)
arturtle.speed(3)

count = 0
count2 = 0

# first initial 'A'
arturtle.left(75)
arturtle.forward(100)
arturtle.right(150)
arturtle.forward(100)
arturtle.backward(50)
arturtle.right(105)
arturtle.forward(26)

#pick pen up and move
arturtle.penup()
arturtle.backward(120)
arturtle.right(90)
arturtle.forward(48)
arturtle.pendown()

# last initial 'G'
arturtle.left(90)
arturtle.forward(50)
arturtle.left(90)
arturtle.forward(95)
arturtle.left(90)
arturtle.forward(50)
arturtle.left(90)
arturtle.forward(45)
arturtle.left(90)
arturtle.forward(25)

# at the end, keep the window open until closed
win.mainloop()
