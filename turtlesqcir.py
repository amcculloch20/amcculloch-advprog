import turtle

window = turtle.Screen()

nick = turtle.Turtle()
nick.speed(50)

for i in range(45):

    nick.penup()
    nick.forward(100)
    nick.pendown()

    nick.forward(20)
    nick.right(90)
    nick.forward(20)
    nick.right(90)
    nick.forward(20)
    nick.right(90)
    nick.forward(20)

    nick.penup()
    nick.setposition(0,0)
    nick.right(2)

window.exitonclick()
