import turtle


def draw_shape(shape,dim):
    window = turtle.Screen()
    window.bgcolor("pink")
    Tilly = turtle.Turtle("turtle")
    Tilly.shapesize(1,1,5)
    Tilly.color("turquoise")
    Tilly.speed(1)
    Tilly.pensize(3)
    Tilly.setpos(0,0)
    
    if shape == "square":    
        count = 0
        while count < 4:
            Tilly.forward(dim)
            Tilly.right(90)
            count = count + 1

    if shape == "circle":
        Tilly.left(90)
        Tilly.circle(dim)


    if shape == "triangle":
        count = 0
        Tilly.left(90)
        while count < 3:
            Tilly.forward(dim)
            Tilly.right(120)
            count += 1
        
    


def picture():
    draw_shape("square",100)
    #draw_shape("triangle", 100)
    #draw_shape("circle",100)
    window.exitonclick()

picture()
