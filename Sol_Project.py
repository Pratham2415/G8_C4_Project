import turtle

turtle.penup()
turtle.setposition(100,100)
turtle.pendown()

for i in range(1):
    turtle.shape("square")
    turtle.pencolor("red")
    turtle.circle(40)
    
turtle.penup()
turtle.setposition(100,-60)
turtle.pendown()

for i in range(1):
    turtle.shape("circle")
    turtle.pencolor("green")
    turtle.circle(80)
