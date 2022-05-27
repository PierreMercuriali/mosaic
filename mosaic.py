from PIL import Image, ImageDraw
import math, random

def variation(n,m):
    return random.randint(n,m)

def pickcolor(c, v):
    #returns a close color
    c0 = c[0] + random.randint(-v,v) 
    if c0 > 255:
        c0 = 255
    if 0 > c0:
        c0 = 0
    c1 = c[1] + random.randint(-v,v) 
    if c1 > 255:
        c1 = 255
    if 0 > c1:
        c1 = 0
    c2 = c[2] + random.randint(-v,v) 
    if c2 > 255:
        c2 = 255
    if 0 > c2:
        c2 = 0
    return (c0,c1,c2)


def drawtesson(x, y, c, p, r, vmin,vmax):
    #x, y, color, picture, ratio, variation min and max
    corners = [(x+variation(vmin, vmax), y+variation(vmin, vmax)),
                (x+(r-variation(vmin, vmax)), y),
                (x+(r-variation(vmin, vmax)), y+(r-variation(vmin, vmax))),
                (x, y+(r-variation(vmin, vmax)))
                ]
    draw = ImageDraw.Draw(p)
    draw.polygon(corners, pickcolor(c, 10))
    
    
im = Image.open('zeugma.png')
print("Image source: ", im.size)
ratio = 10 #how much the image blows up
vmin = 0 #minimal variation in tile size
vmax = 2 #maximal variation in tile size
background = (200, 200, 200) #background color

output = Image.new("RGB", (ratio*im.size[0], ratio*im.size[1]), color=background)
print("Preparing background...")
for i in range(ratio*im.size[0]):
    for j in range(ratio*im.size[1]):
        output.putpixel((i,j), pickcolor(background,20))



print("Generating mosaic...")

for i in range(im.size[0]):
    for j in range(im.size[1]):
        color = im.getpixel((i,j))
        drawtesson(ratio*i, ratio*j, color, output, ratio, vmin, vmax)

print("Saving...")
output.save("".join([random.choice("1234567890") for i in range(32)])+".png")