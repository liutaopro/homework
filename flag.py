#五星红旗
import  turtle
turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.pencolor("red")
for i in range(2):
    turtle.forward(438)
    turtle.right(90)
    turtle.forward(292)
    turtle.right(90)
turtle.end_fill()

#主星 
turtle.up()
turtle.goto(-170,145)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()


#第一颗副星
turtle.up()
turtle.goto(-100,183)
turtle.setheading(-30)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

#第二颗副星 
turtle.up()
turtle.goto(-85,150)
turtle.setheading(20)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

#第三颗副星
turtle.up()
turtle.goto(-85,120)
turtle.setheading(5)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()


#第四颗副星 
turtle.up()
turtle.goto(-100,100)
turtle.setheading(330)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

