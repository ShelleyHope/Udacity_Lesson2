import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("pink")
    
    Tilly = turtle.Turtle("turtle")
    Tilly.shapesize(1,1,5)
    Tilly.color("turquoise")
    Tilly.speed(1)
    Tilly.pensize(3)
    
    Tilly.forward(200)
    Tilly.right(90)
    Tilly.forward(200)
    Tilly.right(90)
    Tilly.forward(200)
    Tilly.right(90)
    Tilly.forward(200)
    Tilly.right(90)

    window.exitonclick()


draw_square()
