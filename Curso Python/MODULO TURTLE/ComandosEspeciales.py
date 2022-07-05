import turtle

s = turtle.Screen()
t = turtle.Turtle()
#velocidad
t.speed(10)
#hacer circulos
t.circle(10)
t.speed(10)
t.circle(60)
#circulo relleno
t.dot(40)
#desaparece
t.hideturtle()
t.speed(1)
t.circle(30)
#volver hacer que aparezca
t.showturtle()
t.circle(100)
#movilizar en el eje x
t.setx(100)
#movilizar en el eje y
t.setx(-80)
turtle.done()