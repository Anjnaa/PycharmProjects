# import cv2

# img = cv2.imread("C:\Desktop\Downloads\hirst-1.jpg", 1)
# print(img)
# cv2.imshow("image.jpg", img)
#
# cv2.imwrite("image_copy.jpg", img)

# import colorgram
# rgb_colors = []
# colours = colorgram.extract("image_copy.jpg", 30)
# for values in colours:
#     r = values.rgb.r
#     g = values.rgb.g
#     b = values.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle as t
import random

t.colormode(255)
tim = t

color_list = [(195, 159, 119), (72, 92, 126), (143, 86, 58), (217, 209, 121), (140, 160, 189), (183, 147, 163),
              (29, 32, 46), (175, 159, 43), (57, 34, 24), (119, 72, 92), (140, 174, 155), (80, 114, 81),
              (63, 31, 41), (139, 27, 18), (182, 100, 85), (118, 29, 40), (46, 58, 93), (173, 99, 116),
              (34, 51, 46), (104, 120, 166), (102, 157, 88), (216, 180, 173), (214, 176, 190), (67, 85, 26),
              (163, 209, 190), (181, 187, 211)]
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
total_dots = 100
for dot_count in range(1, total_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
