from turtle import *


#we want to paint a house

#stepone: draw a squae
width(6)
color("red")

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)


#end of square

#drawing a door
begin_fill()
forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
begin_fill()
right(180)
penup()
goto(0, 200)
pendown()
end_fill()
right(30) 
forward(200)

right(120) 
forward(200)

right(30)
penup()
goto(20, 120)
pendown()
forward(30)
left(90)


forward(30)
left(90)


forward(30)
left(90)

forward(30)
left(90)

penup()
goto(180, 120)
pendown()

forward(30)
right(90)

forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
exitonclick()