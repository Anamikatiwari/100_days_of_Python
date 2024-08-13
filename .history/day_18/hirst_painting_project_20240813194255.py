###  colorgrm.py     :  Python library that lets you extract colors from images.
    # pip install colorgram.py
    
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = ()