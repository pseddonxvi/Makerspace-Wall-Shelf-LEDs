import board
import neopixel
from ledPixelsPico import *

nPix = 37
pastelPurple = (255, 100, 255)
seafoamGreen = (50, 255, 50)
white = (255, 255, 150)
red = (255, 0, 0)
blue = (0, 100, 255)
yellow = (255, 165, 0)
orange = (205, 85, 0)
green = (0, 255, 0)

setcolor=seafoamGreen

pix1 = ledPixels(nPix, board.GP2)
pix2 = ledPixels(nPix, board.GP10)
pix3 = ledPixels(nPix, board.GP14)

pix1.brightness = 0.5

pix1.setColor((setcolor))

pix2.brightness = 0.5

pix2.setColor((setcolor))

pix3.brightness = 0.5

pix3.rainbowForever()
#pix3.setColor((setcolor))
