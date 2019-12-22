import turtle

bakgrund = turtle.Screen()
bakgrund.bgcolor('orange')

my_turtle = turtle.Turtle()

my_turtle.speed(0)


def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)


for i in range(100):
    square(100, 90)
    my_turtle.right(11)

# Circle has 360 degrees
# 360/10 -----> 36 perfect
# pick a prime number like 11
