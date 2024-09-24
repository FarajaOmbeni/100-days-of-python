import turtle as t
import random
import colorgram

screen = t.Screen()
screen.screensize(10,10)
# colors = colorgram.extract('day18_turtle/image.jpeg', 30)
# rgb_colors = []
# for i in range(len(colors)):
#     current_color = colors[i]
#     r_value = current_color.rgb.r
#     g_value = current_color.rgb.g
#     b_value = current_color.rgb.b
#     rgb_colors.append((r_value, g_value, b_value))

color_list = [(225, 153, 51), (241, 245, 250), (190, 156, 27), (123, 35, 69), (207, 80, 94), (25, 48, 116), (46, 111, 153), (169, 87, 26), (160, 61, 86), (50, 33, 39), (59, 40, 34), (33, 80, 70), (16, 30, 86), (203, 123, 136), (95, 127, 165), (168, 28, 24), (132, 155, 183), (210, 77, 60), (22, 62, 52), (226, 202, 118), (60, 106, 77), (226, 171, 182), (149, 170, 155), (100, 148, 70), (222, 177, 168), (7, 89, 111), (176, 185, 215)]

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")

def draw_masterpiece(pos_x, pos_y, dot_size, gap_size, x_dots_size, y_dots_size):
    while y_dots_size != 0:
        tim.penup()
        tim.goto(pos_x, pos_y)
        for _ in range(x_dots_size):
            tim.dot(dot_size, random.choice(color_list))
            tim.penup()
            tim.fd(gap_size)
            tim.pendown()
        pos_y += gap_size
        y_dots_size -= 1
        if y_dots_size == 0:
            return

draw_masterpiece(-320, -250, 20, 50, 10, 10)
screen.exitonclick()