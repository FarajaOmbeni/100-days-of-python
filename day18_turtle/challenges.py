import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed(("fastest"))
timmy.shape("turtle")
timmy.color("blue")
#DRAW A SQUARE
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#DASHED LINE
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#Hexagons
# sides = 3
# for _ in range(10):
#     timmy.pencolor(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)
#     sides += 1

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

#Random Walk
# diretions = [0, 90, 180, 270]
# timmy.pensize(10)

# for _ in range(200):
#     timmy.pencolor(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(diretions))

#DRAW CIRCLE
#MY CODE
# i = 0
# while i < 36:
#     timmy.pencolor(random_color())
#     timmy.circle(100)
#     timmy.right(10)
#     i += 1

#LECTURER
def draw_spiralgraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spiralgraph(5)


screen = t.Screen()
screen.exitonclick()