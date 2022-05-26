from PIL import Image, ImageDraw
import math, random

def variation(n,m):
    return random.randint(n,m)

def drawtesson(x, y, c, p, r, vmin,vmax):
    #x, y, color, picture, ratio, variation min and max
    p.putpixel((x,y), c)
    corners = [(x+variation(vmin, vmax), y+variation(vmin, vmax)),
                (x+(r-variation(vmin, vmax)), y),
                (x+(r-variation(vmin, vmax)), y+(r-variation(vmin, vmax))),
                (x, y+(r-variation(vmin, vmax)))
                ]
    draw = ImageDraw.Draw(p)
    draw.polygon(corners, c)
    
    
im = Image.open('cavecanem.png')
print("Image source: ", im.size)
ratio = 20 #how much the image blows up
vmin = 0 #minimal variation in tile size
vmax = 3 #maximal variation in tile size
background = (200, 200, 200) #background color

output = Image.new("RGB", (ratio*im.size[0], ratio*im.size[1]), color=background)
print("Generating mosaic...")

for i in range(im.size[0]):
    for j in range(im.size[1]):
        color = im.getpixel((i,j))
        drawtesson(ratio*i, ratio*j, color, output, ratio, vmin, vmax)

print("Saving...")
output.save("".join([random.choice("1234567890") for i in range(32)])+".png")