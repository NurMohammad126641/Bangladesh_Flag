import turtle

def draw_bangladesh_map():
    screen = turtle.Screen()
    screen.title("Bangladesh Map")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("green")
    pen.width(1)
    pen.speed(2)

    # Drawing the outline of Bangladesh
    pen.penup()
    pen.goto(-150, 100)
    pen.pendown()
    pen.begin_fill()
    pen.forward(300)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(300)
    pen.right(90)
    pen.forward(200)
    pen.end_fill()

    # Drawing the center circle
    pen.penup()
    pen.goto(45, 0)  # Adjusted position to center the circle
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()

# Call the function to draw the map
draw_bangladesh_map()
