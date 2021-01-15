def coloredCircle(turtle,penColor,fillColor,radius,penSize):
    turtle.color(penColor,fillColor)
    turtle.pensize(penSize)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()