#Exercise-1
def draw_circles(t, size, decrease_amount):
    for _ in range(4):
        t.circle(size)
        size = size - decrease_amount
import turtle


t = turtle.Turtle()


screen = turtle.Screen()


draw_circles(t, 100, 4)
draw_circles(t, 100, 5)
draw_circles(t, 100, 10)
draw_circles(t, 100, 19)
draw_circles(t, 100, 20)


screen.mainloop()

#Exercise-2
def draw_special(t, size, repeat, decrease_amount):
    for _ in range(repeat):
        draw_circles(t, size, decrease_amount)
        t.right(360 / repeat)
import turtle


t = turtle.Turtle()

screen = turtle.Screen()


draw_special(t, 100, 4, 4)
draw_special(t, 100, 5, 5)
draw_special(t, 100, 6, 10)
draw_special(t, 100, 8, 19)
draw_special(t, 100, 10, 20)

screen.mainloop()

#Exercise-3
import turtle

def draw_circles(t, size, decrease_amount):
    for _ in range(4):
        t.circle(size)
        size = size - decrease_amount

def draw_special(t, size, repeat, decrease_amount):
    for _ in range(repeat):
        draw_circles(t, size, decrease_amount)
        t.right(360 / repeat)

def draw_picture():
    t = turtle.Turtle()
    screen = turtle.Screen()
    
    colours = ['white', 'yellow', 'blue', 'orange', 'pink']
    decrease_amounts = [4, 10, 5, 19, 20]

    for i in range(5):
        t.color(colours[i])
        draw_special(t, 100, 4, decrease_amounts[i])

    screen.mainloop()


draw_picture()

