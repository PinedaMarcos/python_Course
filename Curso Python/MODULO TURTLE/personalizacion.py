import turtle

s = turtle.Screen()
t = turtle.Turtle()

#darle color al lienzo
s.bgcolor("blue")
#nombre del lienzo
s.title("Project1")
#modificar tamaño de la tortuga
t.shapesize(3,3 ,3)
#color a la tortuga
t.fillcolor("Red")
#cambiar color de la tinta(linea)
t.pencolor("White")
t.forward(100)
#aumentar el ancho de la tinta
t.pensize(5)
#rellenar figuras
t.begin_fill()
t.circle(150)
t.end_fill()

turtle.done()