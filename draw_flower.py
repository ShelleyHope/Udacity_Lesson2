import turtle

def draw_stem(some_turtle):
    some_turtle.color("green")
    some_turtle.pensize(6)
    some_turtle.setpos(0,-400)
    some_turtle.pendown()
    some_turtle.left(90)
    some_turtle.forward(400)
    some_turtle.penup()


def draw_petals(some_turtle):
    some_turtle.color("violet")
    some_turtle.pensize(2)
    some_turtle.setpos(-10,15)
    some_turtle.pendown()
    count = 0
    while count < 91:
        for i in range(1, 14):
            some_turtle.forward(90)
            some_turtle.left(174)
            some_turtle.forward(86.415)
            some_turtle.left(90)
            some_turtle.forward(25.147)
            count += 1
            some_turtle.left(5)

def draw_stamen(some_turtle):
    some_turtle.penup()
    some_turtle.setpos(5,10)
    some_turtle.color("yellow")
    some_turtle.pensize(9)
    some_turtle.pendown()
    some_turtle.circle(9)
 

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("turquoise")
    window.screensize(600,600)

    Tilly = turtle.Turtle()
    Tilly.ht()
    Tilly.speed(50)
    draw_stem(Tilly)
    draw_petals(Tilly)
    draw_stamen(Tilly)
    
    window.exitonclick()

    
draw_flower()
    
    
