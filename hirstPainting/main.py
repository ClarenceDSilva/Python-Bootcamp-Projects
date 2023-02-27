import colorgram
import random
import turtle as t

t.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg',25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
tim = t.Turtle()
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
              (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (166, 204, 202), (62, 26, 45),
              (145, 165, 181), (6, 79, 111)]

# origin()
pace = 0
tim.hideturtle()
tim.penup()
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    pace += 50
    # tim.goto(0, pace)
    tim.home()
    tim.left(90)
    tim.forward(pace)
    tim.right(90)


def origin():
    tim.setheading(225)
    tim.penup()
    tim.forward(300)
    tim.setheading(0)
