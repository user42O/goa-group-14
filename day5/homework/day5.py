from turtle import *

#house number 1 
speed(0)
begin_fill()
penup()
backward(450)
pendown()
color("darkblue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(75)
end_fill()
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()
color("darkblue")
forward(75)
right(90)
forward(200)
color("yellow")
begin_fill()
right(45)
forward(141)
right(90)
forward(141)
end_fill()
color("darkblue")
right(45)
forward(200)
right(90)
forward(75)
color("yellow")
forward(50)
color("yellow")
right(90)
forward(100)
color("darkblue")
forward(30)
color("yellow")
begin_fill()
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
left(90)
penup()
forward(25)
left(90)
pendown()
color("darkblue")
forward(40)
penup()
left(90)
forward(25)
left(90)
forward(20)
left(90)
pendown()
forward(50)
penup()
color("darkblue")


goto(-200,0)


#house number 2

pendown()
begin_fill()
color("darkblue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(75)
end_fill()
begin_fill()
color("yellow")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()
color("darkblue")
forward(75)
right(90)
forward(200)
color("yellow")
begin_fill()
right(45)
forward(141)
right(90)
forward(141)
end_fill()
color("darkblue")
right(45)
forward(200)
right(90)
forward(75)
color("yellow")
forward(50)
color("yellow")
right(90)
forward(100)
color("darkblue")
forward(30)
color("yellow")
begin_fill()
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
left(90)
penup()
forward(25)
left(90)
pendown()
color("darkblue")
forward(40)
penup()
left(90)
forward(25)
left(90)
forward(20)
left(90)
pendown()
forward(50)
penup()
color("darkblue")


#house number 3

goto(50,0)

begin_fill()
pendown()
color("darkblue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(75)
end_fill()
begin_fill()
color("yellow")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()
color("darkblue")
forward(75)
right(90)
forward(200)
color("yellow")
begin_fill()
right(45)
forward(141)
right(90)
forward(141)
end_fill()
color("darkblue")
right(45)
forward(200)
right(90)
forward(75)
color("yellow")
forward(50)
color("yellow")
right(90)
forward(100)
color("darkblue")
forward(30)
color("yellow")
begin_fill()
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
left(90)
penup()
forward(25)
left(90)
pendown()
color("darkblue")
forward(40)
penup()
left(90)
forward(25)
left(90)
forward(20)
left(90)
pendown()
forward(50)
penup()
color("darkblue")
left(90)

#garden
speed(0)
penup()
goto(-450,-50)
pendown()

color("green")
length = 40
distance = 3
#

for x in range(120):
    forward(length)
    penup()
    right(90)
    forward(distance)
    right(90)
    pendown()
    forward(length)
    penup()
    left(90)
    forward(distance)
    left(90)
    pendown()
#  
    

#sun
    
penup()
goto(-380,300)


def draw_circle(radius, color):
    penup()
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

speed(5)
draw_circle(50, 'yellow')

hideturtle()
exitonclick()



























































































































































exitonclick()
