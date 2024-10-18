from turtle import *

speed(40)

width(7)

color("red")
begin_fill()
left(180)         #start
forward(80)
right(90)
forward(120)      #height

left(45)
forward(30)
right(45)
forward(20)      #1
right(90)
forward(20)   #2
right(90)
forward(10)     #3
left(90)
forward(25)    #4
left(90)
forward(10)    #5
right(90)
forward(30)   #6

right(90)
forward(10)
penup()
goto(0,0)
pendown()
left(180)
forward(120)
right(45)
forward(30)
left(45)
forward(20)
left(90)
forward(20)
left(90)

forward(10)
right(90)
forward(25)
end_fill()

goto(0,0)

right(180)      
forward(200)
forward(80)

goto(200,0)

begin_fill()

left(90)
forward(120)     #height
left(45)      
forward(30)
right(45)

forward(20)
right(90)
forward(20)
right(90)
forward(10)
left(90)
forward(25)
left(90)
forward(10)

right(90)
forward(30)
right(90)
forward(10)
left(90)
forward(20)

goto(280,0)
end_fill()

begin_fill()
left(90)

forward(120)
right(45)
forward(30)
left(45)
forward(20)
left(90)
forward(20)
left(90)
forward(10)
right(90)
forward(10)
end_fill()

goto(200,0)

begin_fill()
right(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()


left(90)
forward(75)
color("black")     #
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




















exitonclick()