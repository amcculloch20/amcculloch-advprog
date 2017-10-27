import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

nick = turtle.Turtle()      # create a turtle named nick
nick.forward(2000)           # tell nick to move forward by 150 units
nick.left(1)               # turn by 90 degrees
nick.forward(2000)            # complete the second side of a rectangle

window.exitonclick()
