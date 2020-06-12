__author__ = "Andrew Peña"
__credits__ = ["Andrew Peña", "Malcolm Johnson"]
__version__ = "0.1.0"
__status__ = "Prototype"
from PIL import Image, ImageDraw

"""This program takes an image and tiles it, vertically and horizontally, and
adds a colored line to the bottom of each row of images. It also crops the top
and the left side of the image in order to fit certain software.
Currently, these values must be hard-coded; that is, user input is not accepted
after the script has been run.

Parameters:
newImMultH -- The number of tiles, vertically. Do NOT set below 1.
newImMultW -- The number of tiles, horizontally. Do NOT set below 1.
topMarginCutoff -- The number of pixels to remove from the top.
leftMarginCutoff -- The number of pixels to remove from the left.
lineThiccness -- The thickness, in pixels, of the line being add to the bottom
    of each row.
lineColor -- The color of the line in RGB, expressed as a 3-tuple.
"""
newImMultH = 20
newImMultW = 20
topMarginCutoff = 0
leftMarginCutoff = 0
lineThiccness = 0
lineColor = (255, 80, 80)

## Do not edit past this point
im = Image.open("square.jpg")
newHeight = im.height * newImMultH
newWidth = im.width * newImMultW
lineOffset = lineThiccness / 2
newIm = Image.new("RGB", (newWidth, newHeight))
draw = ImageDraw.Draw(newIm)
r = 0
c = 0
while r < newImMultH:
    while c < newImMultW:
        newIm.paste(im, (im.width * c, im.height * r))
        c += 1
    r += 1
    draw.line((0, (im.height * r) - lineOffset, newWidth,
    (im.height * r) - lineOffset), lineColor, lineThiccness)
    c = 0
newIm = newIm.crop((leftMarginCutoff, topMarginCutoff, newWidth, newHeight))
newIm.save("output.png")
