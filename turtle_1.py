import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
turtle.bgcolor("black")  # Background color

# List of colors to use in the design
colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw the design
def draw_design():
    size = 300  # Initial size of the square
    for i in range(69):
        t.color(colors[i % len(colors)])
        draw_square(size)
        t.right(10)
        size -= 5  # Decrease the size of the square for each iteration

# Position the turtle
t.penup()
t.goto(-150, 150)
t.pendown()

# Draw the design
draw_design()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
