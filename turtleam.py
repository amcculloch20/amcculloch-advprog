import turtle

window = turtle.Screen()
nick = turtle.Turtle()

nick.speed(10)

#A
nick.right(120)
nick.forward(300)
nick.penup()
nick.setposition(0,0)
nick.left(120)
nick.pendown()
nick.right(80)
nick.forward(300)
nick.penup()
nick.setposition(0,0)
nick.forward(150)
nick.pendown()
nick.right(110)
nick.forward(105)

nick.penup()
nick.setposition(0,0)
nick.left(140)
nick.pendown()

#S
nick.circle(75,180)
nick.circle(-75,180)

nick.penup()
nick.setposition(0,0)
nick.pendown()
nick.right(190)

#M
nick.forward(300)
nick.penup()
nick.setposition(0,0)
nick.pendown()
nick.left(30)
nick.forward(300)
nick.left(150)
nick.forward(300)
nick.right(150)
nick.forward(300)
window.exitonclick()
