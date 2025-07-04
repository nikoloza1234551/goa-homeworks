from turtle import *

shape("turtle")
speed(30)
width(7)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#now we are drawing door

forward(70)
color("black")
begin_fill()
left(90)


forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()
#end of drawing a door

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

penup()
goto(200, 0)
pendown()

left(120)

begin_fill()
color("green")
forward(170)


#aq shevcvale
left(180)
forward(500)
left(90)
forward(250)
left(90)
forward(670)

left(90)
forward(250)
end_fill()
exitonclick()
