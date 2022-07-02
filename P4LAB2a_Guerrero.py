# Turtle Graphics
# CTI-110
# 7/2/22
# Arturo Guerrero

#initialize
import turtle
win = turtle.Screen()

# make your turtle
arturtle = turtle.Turtle()
arturtle.shape("turtle")
arturtle.speed(3)

count = 0
count2 = 0

while count < 8:
    count += 1
    while count2 <= 3:
        arturtle.forward(50)
        arturtle.right(90)
        count2 += 1
    while count2 <= 6:
        arturtle.left(120)
        arturtle.forward(50)
        count2 +=1

# at the end, keep the window open until closed
win.mainloop()