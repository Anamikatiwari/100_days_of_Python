###  colorgrm.py     :  Python library that lets you extract colors from images.
    # pip install colorgram.py
    
import colorgram

colors = colorgram.extract('image.jpg', 30)
for color in colors