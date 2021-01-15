import turtle
import drawing

pet = turtle.Turtle()

pet.speed(100)

drawing.coloredCircle(pet,"teal","forestgreen",75,5)

pet.penup()
pet.setx(100)
pet.sety(100)
pet.pendown()

drawing.coloredCircle(pet,"teal","forestgreen",75,5)

pet.penup()
pet.setx(-200)
pet.sety(-200)
pet.pendown()

drawing.coloredCircle(pet,"teal","forestgreen",75,5)

#drawing.coloredCircle(pet,"teal","forestgreen",75,5)

pet.penup()
pet.setx(-100)
pet.sety(-100)
pet.pendown()

drawing.coloredCircle(pet,"teal","forestgreen",75,5)

pet.left(180)

pet.penup()
pet.setx(250)
pet.sety(250)
pet.pendown()

drawing.coloredCircle(pet,"teal","forestgreen",75,5)

turtle.done()