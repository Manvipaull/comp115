#Exercise-1
import turtle
def draw_square(side_length):
    """ Draw a square whose side length equals the value of side_length """
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / 4 
    for _ in range(4):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()


draw_square(40)


#Exercise-2
import turtle
def draw_regular_polygon(num_sides, side_length):
    """ Draw an arbitrary regular polygon,
    when given a number of sides, and a side_length"""
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / num_sides 
    for _ in range(num_sides):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()


draw_regular_polygon(8, 50)

#Exercise-3
import turtle
def draw_rectangle(length, width):
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.shape("blank")
    pen.clear()


draw_rectangle(40, 20)


#Exercise-4
import turtle
def draw_circles(num_circles):
    radius = 10 
    radius_increase = 5
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(num_circles):
        pen.circle(radius)
        radius = radius + radius_increase
    pen.shape("blank")
    pen.clear()


draw_circles(7)
