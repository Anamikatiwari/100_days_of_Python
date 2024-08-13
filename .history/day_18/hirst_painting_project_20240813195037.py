###  colorgrm.py     :  Python library that lets you extract colors from images.
    # pip install colorgram.py
    
 #-------------------------------------------------------------------------   
    
    
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

#-----------------------------------------------------------------------------------------------------


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

tim.dot(20, random.choice(color_list))

screen = turtle_module.Screen